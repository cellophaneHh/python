"""
想请求中添加请求头
"""
import requests

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

print(r.encoding)
print(r.text)
