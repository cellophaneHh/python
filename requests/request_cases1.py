import requests

r = requests.get('https://api.github.com/events')
print(type(r))

# post请求
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r.text)
# put请求
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r.text)

# delete
r = requests.put('http://httpbin.org/delete')
print(r.text)

# head
r = requests.head('http://httpbin.org/get')
print(r.headers)

# options
r = requests.options('http://httpbin.org/get')
print(r.text)
print(r.headers)


# 传递参数, 不会添加None值
payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
r = requests.get('http://httpbin.org/get', payload)
print(r.url)

# 传递列表
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# 读取相应
r = requests.get('https://api.github.com/events')

with open('sources/github_api.json', 'w') as api:
    api.write(r.text)

