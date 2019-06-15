from resources.user_agent import USER_AGENT_FIREFOX
from lxml import etree
from mongo.mongo import db
from redisclient.redis_pool import redis_client
from log_handler import LogHandler
import time
import os
import urllib
import asyncio
import aiohttp

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
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(
            ssl=False))
        self.detail_urls_queue = asyncio.Queue(maxsize=100)
        # 并发2
        self.download_semaphore = asyncio.Semaphore(2000)
        # 详情页过滤器
        self.detail_urls_raw_bloom_filter = "detail_urls_raw_bloom_filter"
        if not redis_client.exists(self.detail_urls_raw_bloom_filter):
            redis_client.execute_command("bf.reserve {} {} {}".format(
                self.detail_urls_raw_bloom_filter, 0.001, 100000000))
        self.detail_html_source_bloom_filter = "detail_html_source_bloom_filter"
        if not redis_client.exists(self.detail_html_source_bloom_filter):
            redis_client.execute_command("bf.reserve {} {} {}".format(
                self.detail_html_source_bloom_filter, 0.001, 100000000))

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

    async def __add_baike_detail_urls_raw(self, url):
        db.baike_detail_urls_raw.update_one({'url': url},
                                            {'$set': {
                                                'url': url
                                            }},
                                            upsert=True)

    async def __extend_detail_urls(self, root_url, detail_html_source):
        '''由种子url采集到的页面获取的细览页'''
        try:
            parser = etree.HTML(detail_html_source)
            detail_urls = parser.xpath(
                "//div[@class='before-content']/div[@class='polysemant-list polysemant-list-normal']//ul/li[@class='item']/a/@href|//div[@class='content'][1]//a[starts-with(@href, '/item')]/@href"
            )

            log.info("扩展细览页数量: {} {}".format(len(detail_urls), root_url))
            tasks = []
            for detail_url in detail_urls:
                absolute_detail_url = urllib.parse.unquote(self.baike_home +
                                                           detail_url)
                if self.__detail_urls_raw_exists(absolute_detail_url):
                    continue
                tasks.append(
                    self.__add_baike_detail_urls_raw(absolute_detail_url))
            if tasks:
                await asyncio.wait(tasks, timeout=5)
        except Exception as e:
            raise e

    async def __download(self, url):
        async with self.session.get(url, headers=self.header,
                                    timeout=60) as response:
            status = response.status
            response.encoding = 'utf-8'
            if status == 200:
                return await response.text()
            log.error("下载失败: {} {}".format(url, status))

    def __detail_html_source_exists(self, url):
        '''是否已经下载过'''
        result = redis_client.execute_command("bf.exists {} {}".format(
            self.detail_html_source_bloom_filter, urllib.parse.quote(url)))
        return result == 1

    def __detail_html_source_add(self, url):
        return redis_client.execute_command('bf.add {} {}'.format(
            self.detail_html_source_bloom_filter, urllib.parse.quote(url)))

    def __detail_urls_raw_exists(self, url):
        '''细览页url是否已经存在'''
        result = redis_client.execute_command("bf.exists {} {}".format(
            self.detail_urls_raw_bloom_filter, urllib.parse.quote(url)))
        return result == 1

    def __detail_urls_raw_add(self, url):
        return redis_client.execute_command('bf.add {} {}'.format(
            self.detail_urls_raw_bloom_filter, urllib.parse.quote(url)))

    async def __async_detail_content(self):
        '''获取细览页源码，可独立运行, 异步版本, 获取队列中的url,消费者'''
        while True:
            try:
                url = await self.detail_urls_queue.get()
                self.detail_urls_queue.task_done()
                if self.__detail_html_source_exists(url):
                    continue
                log.info("开始获取细览页内容: {}".format(url))
                try:
                    html_source = await self.__download(url)
                    if html_source:
                        await asyncio.ensure_future(
                            self.__extend_detail_urls(url, html_source))
                        db.baike_detail_html_source.update_one(
                            {"url": url},
                            {"$set": {
                                "url": url,
                                "html_source": html_source
                            }},
                            upsert=True)
                        self.__detail_html_source_add(url)
                except Exception as e:
                    log.error("采集失败: {}, {}".format(url, repr(e)))
                finally:
                    pass
            except Exception as cause:
                log.error('采集失败: {}'.format(repr(cause)))
            finally:
                pass

    async def __new_task_to_queue(self):
        '''向队列中增加url,生产者'''
        # 初始化过滤器中的元素
        # cursor = db.baike_detail_urls_raw.find(batch_size=5000)
        # for doc in cursor:
        #     print(doc['url'])
        #     self.__detail_urls_raw_add(doc['url'])
        # 生产者队列
        while True:
            cursor = db.baike_detail_urls_raw.find(batch_size=5000)
            for doc in cursor:
                await self.detail_urls_queue.put(doc['url'])
            log.info('queue_size: {}'.format(self.detail_urls_queue.qsize()))

    async def async_execute(self, loop):
        consumers = [
            loop.create_task(self.__async_detail_content()) for i in range(100)
        ]
        producer = loop.create_task(self.__new_task_to_queue())
        await asyncio.wait(consumers + [producer])

    def execute(self):
        self.__detail_content()


baike = BaiduBaike()
loop = asyncio.get_event_loop()
loop.run_until_complete(baike.async_execute(loop))
