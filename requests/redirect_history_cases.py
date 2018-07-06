"""
重定向与请求历史
"""
import requests

r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)
print(len(r.content))

# 禁止重定向
r = requests.get('http://github.com', allow_redirects=False)
print(r.url)
print(r.status_code)
print(r.history)
