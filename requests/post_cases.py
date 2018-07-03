"""
post请求参数放在data参数中
"""
import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('http://httpbin.org/post', data=payload)

print(r.text)

# payload可以为一个元组列表， 存在某些key相同的情况

payload = (('key1', 'value1'), ('key1', 'value2'))

r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

# 传数组，对比上面元组列表相同的key，没有差别
payload = {'key1': ['value1', 'value2']}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

