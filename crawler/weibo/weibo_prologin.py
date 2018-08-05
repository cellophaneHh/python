import requests
import json
import time

cookie_here = 'SINAGLOBAL=172.16.92.26_1533454611.976624; SCF=AsYm-8NQFWrarPNriRTdhKu6BrzR7FAvvIBrY0qFq7HtyHYVdLhf4WmpYa_9_UP9Z4RgoGpY1T7x1qL4kMYaBvw.; SUB=_2AkMsOiLgdcPxrAJZm_wSzW_kaY5H-jyf70sWAn7tJhMyAhgv7mkfqSVutBF-XIhNfPCwIbyOlXeVDiUGaSc4uf9p; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WFr6rZm6kIiqB.if_ZxUW5R5JpVF02RSK2Re0npSK-N;'

header = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.75 Chrome/68.0.3440.75 Safari/537.36",
    'cookie': cookie_here,
}

prelogin_url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTg1MTgzODE1NTc=&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_='

# 链接加时间戳
prelogin_url = prelogin_url + str(round(time.time() * 1000))

session = requests.Session()
res = session.get(prelogin_url, headers=header)
json_str = res.content.decode('gbk')
print(json_str)
