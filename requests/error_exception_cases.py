"""
错误与异常
"""
import requests
try:
    r = requests.get('https://www.baidu.com')
    print(r.status_code)
except RequestException:
    print('异常')

