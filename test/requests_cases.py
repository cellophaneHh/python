'''
谷歌为啥访问不了呢。。。
'''
import requests
import json

header = {
    "user-agent":
    "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
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

url = "https://baike.baidu.com/wikitag/api/getlemmas"
params = {
    "limit": 24,
    "timeout": 3000,
    "filterTags": [],
    "tagId": 76607,
    "fromLemma": False,
    "contentLength": 40,
    "page": 1
}

res = requests.post(url, data=params, headers=header)
if res.status_code == 200:
    jsonresult = json.loads(res.text)
    print(jsonresult["lemmaList"][0])
