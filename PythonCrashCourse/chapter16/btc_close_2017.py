"""
下载
"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from urllib.request import urlopen

import json
import requests

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
response = urlopen(json_url)

# 读取数据
req = response.read()
# print(type(req))
# print(req)
# 将数据写入文件
with open("btc_close_2017_down.json", 'wb') as f:
    f.write(req)

# 加载json格式
# with open("btc_close_2017_down.json", 'r') as f:
#     file_urllib = json.load(f)
#     print(file_urllib)
file_urllib = json.loads(str(req, 'utf-8'))
print(file_urllib)

# 使用requests

req = requests.get(json_url)
with open('btc_close_2017_down_requests.json', 'w') as f:
    f.write(req.text)

print(req.json())

