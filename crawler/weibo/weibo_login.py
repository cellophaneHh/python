import requests
import json
import time

header = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.75 Chrome/68.0.3440.75 Safari/537.36"
}

login_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)&_=';
data = {
    'cdult': 2,
    'domain': 'weibo.com',
    'encoding': 'UTF-8',
    'entry': 'weibo',
    'from': '',
    'gateway': 1,
    'nonce': '1PU6DS',
    'pagerefer': 'https://login.sina.com.cn/crossdomain2.php?action=logout&r=https%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F',
    'prelt': 56,
    'pwencode': 'rsa2',
    'qrcode_flag': False,
    'returntype': 'TEXT',
    'rsakv': 1330428213,
    'savestate': 7,
    'servertime': 1533457773,
    'service': 'miniblog',
    'sp': 'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443',
    'sr': '975*550',
    'su': 'MTg1MTgzODE1NTc=',
    'useticket': 1,
    'vsnf': 1,
}
# 链接加时间戳
login_url = login_url + str(round(time.time() * 1000))

session = requests.Session()
res = session.post(login_url, data=data, headers=header)
json_str = res.content.decode('gbk')
info = json.loads(json_str)
print(info)

