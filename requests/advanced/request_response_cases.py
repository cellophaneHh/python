"""
请求和响应
"""

import requests

r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
# 获得响应头
print(r.headers)
# 获得请求头
print(r.request.headers)

