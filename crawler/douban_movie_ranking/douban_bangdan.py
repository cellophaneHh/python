'''
豆瓣电影一周口碑榜和北美票房榜
'''
import requests
from lxml import etree
from db.redis_pool import redis_client
import time
from crawler_config import movieInfoConfig
import json

html_source_key = "html_source"
html_source_detail = "html_source_detail"
movie_info = "movie_info"


class DouBanMovieRanking:
    def __init__(self):
        self._srcUrl = "https://movie.douban.com/chart"
        self._headers = {
            "user-agent":
            "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
            "accept-encoding": "gzip, deflate"
        }
        self._week_ranking_url_path = "//div[@id='ranking']/div[@id='ranking'][1]/ul/li/div[@class='name']/a/@href"
        self._north_american_ranking_url_path = "//div[@id='ranking']/div[@id='ranking'][2]/ul/li/div[2]/a/@href"
        self.__init()

    def __init(self):
        self.session = requests.Session()
        self.session.headers.update(self._headers)

    def __html_source(self, key, url, force_download=False):
        """源码下载"""
        content = ""
        if not force_download and not self.__exist(key, url):
            res = self.session.get(url)
            res.encoding = "utf8"
            if res.status_code == 200:
                redis_client.hset(key, url, res.text)
                content = res.text
        else:
            content = redis_client.hget(key, url)
        return content

    def __exist(self, key, url):
        return redis_client.hexists(key, url)

    def __week_ranking_url(self):
        """周榜url"""
        html = etree.HTML(self.__html_source(html_source_key, self._srcUrl))
        return html.xpath(self._week_ranking_url_path)

    def __north_american_ranking_url(self):
        """北美排行榜url"""
        html = etree.HTML(self.__html_source(html_source_key, self._srcUrl))
        return html.xpath(self._north_american_ranking_url_path)

    def execute(self):
        urls = []
        urls.extend(self.__week_ranking_url())
        urls.extend(self.__north_american_ranking_url())

        for url in urls:
            if not self.__exist(html_source_detail, url):
                html = etree.HTML(self.__html_source(html_source_detail, url))
                movieDetail = {}
                for name, xpath in movieInfoConfig.items():
                    movieDetail[name] = html.xpath(xpath)
                    redis_client.hset(
                        movie_info, url,
                        json.dumps(movieDetail, ensure_ascii=False))
                    time.sleep(4)


dbr = DouBanMovieRanking()
dbr.execute()
print("finished...")
