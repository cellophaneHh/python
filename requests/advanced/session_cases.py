import requests

# 会话可以用来跨请求保存cookie
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)

# 会话可以为请求方法提供缺省数据,缺省数据跨请求保持

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
print(type(s.headers))
print(s.headers)
# 请求中设置的数据会随之一起发送，但是不能跨请求保持
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
# {"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Authorization":"Basic dXNlcjpwYXNz","Connection":"close","Host":"httpbin.org","User-Agent":"python-requests/2.19.1","X-Test":"true","X-Test2":"true"}}

