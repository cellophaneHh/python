import requests
from resources.user_agent import USER_AGENT_FIREFOX
from lxml import etree
from redisclient.redis_pool import redis_client
from log_handler import LogHandler
import time
import os
import urllib

log = LogHandler("baidubaike")


class BaiduBaike:
    def __init__(self):
        # 百科首页
        self.baike_home = "http://baike.baidu.com"
        # 请求头
        self.header = {
            "user-agent": USER_AGENT_FIREFOX,
            "host": "baike.baidu.com",
            "accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language":
            "zh-CN,en-US;q=0.8,zh;q=0.7,zh-TW;q=0.5,zh-HK;q=0.3,en;q=0.2",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "upgrade-insecure_requests": "1",
            "cache-control": 'max-age=0',
        }
        self.session = requests.Session()

    def __fenlei_url(self):
        '''所有分类的url, 可独立运行'''
        res = self.session.get(self.baike_home, headers=self.header, timeout=5)
        res.encoding = "utf-8"
        if res.status_code == 200:
            html_source = res.text
            parser = etree.HTML(html_source)
            alist = parser.xpath(
                "//div[@id='commonCategories']//div[@class='column']/a/@href")
            pipeline = redis_client.pipeline()
            for a in alist:
                if a.startswith("/fenlei"):
                    pipeline.rpush(self.baike_home + ":common_categories",
                                   self.baike_home + a)
                    pipeline.execute()
                else:
                    log.info(res.reason)

    def __detail_url(self, root_url, url):
        '''分类中每个词条的url，带翻页'''
        log.info("start: {}".format(url))
        res = self.session.get(url, headers=self.header, timeout=5)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            html_source = res.text
            parser = etree.HTML(html_source)
            detail_urls = parser.xpath(
                "//div[@class='grid-list grid-list-spot']/ul/li/div[@class='list']/a/@href"
            )
            log.info("detail_count: {}".format(len(detail_urls)))
            pipeline = redis_client.pipeline()
            for detail_url in detail_urls:
                pipeline.sadd("baike_detail_urls_raw",
                              self.baike_home + detail_url)
            pipeline.execute()
            # 翻页
            next_page_urls = parser.xpath(
                "//div[@class='page']//a[@id='next']/@href")
            if next_page_urls:
                next_page_url = os.path.dirname(
                    root_url) + "/" + next_page_urls[0]
                log.info('next: {}'.format(next_page_url))
                time.sleep(5)
                self.__detail_url(root_url, next_page_url)
        else:
            log.info(res.reason)

    def __detail_urls(self):
        '''分类url采集到的种子url, 可独立运行'''
        urls = redis_client.lrange(self.baike_home + ":common_categories", 0,
                                   -1)
        for url in urls:
            self.__detail_url(url, url)
            log.info("finish: {}".format(url))
            time.sleep(5)

    def __extend_detail_urls(self, root_url, detail_html_source):
        '''由种子url采集到的页面获取的细览页'''
        try:
            parser = etree.HTML(detail_html_source)
            detail_urls = parser.xpath(
                "//div[@class='before-content']/div[@class='polysemant-list polysemant-list-normal']//ul/li[@class='item']/a/@href|//div[@class='content'][1]//a[starts-with(@href, '/item')]/@href"
            )
            pipeline = redis_client.pipeline()
            log.info("extend_detail_urls count: {}".format(len(detail_urls)))
            for detail_url in detail_urls:
                absolute_detail_url = urllib.parse.unquote(self.baike_home +
                                                           detail_url)
                pipeline.sadd("baike_detail_urls_raw", absolute_detail_url)
            pipeline.execute()
        except Exception as e:
            raise e

    def __detail_content(self):
        '''获取细览页源码，可独立运行'''
        detail_urls_result = redis_client.sscan("baike_detail_urls_raw",
                                                0,
                                                count=10)
        while True:
            cursor, detail_urls = detail_urls_result
            log.info("detail_root_count: {}".format(len(
                detail_urls_result[1])))
            for url in detail_urls:
                try:
                    log.info("url: {}".format(url))
                    if redis_client.hexists("baike_detail_html_source", url):
                        log.info("重复跳过: {}".format(url))
                        continue
                    log.info("detail_content: {}".format(url))
                    res = self.session.get(url, headers=self.header, timeout=5)
                    res.encoding = 'utf-8'
                    if res.status_code == 200:
                        html_source = res.text
                        self.__extend_detail_urls(url, html_source)
                        redis_client.hset("baike_detail_html_source", url,
                                          html_source)
                    else:
                        log.info("采集失败: {}, {}".format(url, res.reason))
                except Exception as e:
                    log.error("采集失败: {} {}".format(url, e))
                else:
                    redis_client.sadd("baike_detail_urls_raw", url)
                finally:
                    time.sleep(5)
            # 大于1千万的时候停止
            count = redis_client.hlen("baike_detail_html_source")
            if count > 10000000:
                break
            detail_urls_result = redis_client.sscan("baike_detail_urls_raw",
                                                    cursor,
                                                    count=10)
            log.info("下一循环...")

    def execute(self):
        self.__detail_content()


baike = BaiduBaike()
baike.execute()
