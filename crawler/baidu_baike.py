import requests
from resources import user_agent
from lxml import etree
from redisclient.redis_pool import redis_client
from log_handler import LogHandler

log = LogHandler()

# 百科首页
baike_home = "http://baike.baidu.com"
# 请求头
header = {
    "user-agent": user_agent.USER_AGENT_FIREFOX,
    "host": "baike.baidu.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-language": "zh-CN,en-US;q=0.8,zh;q=0.7,zh-TW;q=0.5,zh-HK;q=0.3,en;q=0.2",
    "accept-encoding": "gzip, deflate, br",
    "connection": "keep-alive",
    "upgrade-insecure_requests": "1",
    "cache-control": 'max-age=0',
}
session = requests.Session()
res = session.get(baike_home, headers=header, timeout=5)
res.encoding="utf-8"

if res.status_code == 200:
    html_source = res.text
    parser = etree.HTML(html_source)
    alist = parser.xpath("//div[@id='commonCategories']//div[@class='column']/a/@href")
    pipeline = redis_client.pipeline()
    for a in alist:
        if a.startswith("/fenlei"):
            pipeline.rpush(baike_home + ":common_categories", baike_home + a)
    pipeline.execute()
else:
    log.info(res.reason)
