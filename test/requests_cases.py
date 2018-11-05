'''
谷歌为啥访问不了呢。。。
'''
import requests
import json
from lxml import etree


def get_proxy():
    # return 'socks5://127.0.0.1:1080'
    r = requests.get('http://193.112.95.23:5010/get/')
    if r.status_code == 200:
        return r.text


proxy = get_proxy()
proxies = {
    'http': proxy,
    'https': proxy,
}
headers = {
    'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
session = requests.Session()
print(session.headers)
print(proxies)
r = session.get('http://www.beautylegmm.com/photo/beautyleg/2018/1673/beautyleg-1673-0001.jpg',
                proxies=proxies, headers=headers, timeout=5)
print('1')
if r.status_code == 200:
    print('ok...')
else:
    print('failure...')
