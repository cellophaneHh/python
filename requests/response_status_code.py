"""
响应状态码
"""
import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(type(r.headers))
print(r.headers['content-type'])


bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
try:
    print(bad_r.raise_for_status())
except RequestException:
    print('异常')
