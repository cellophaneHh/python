"""
请求提中直接放string
"""
import requests
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))

print(r.text)
print(r.headers)

r = requests.post(url, json=payload)
print(r.text)
print(r.headers)

