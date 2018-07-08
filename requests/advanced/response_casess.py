"""
响应体内容工作流
默认情况下，请求后响应体立即被下载，
可以通过stream参数设置为访问Response.content时才延迟下载
"""

import requests

tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
r = requests.get(tarball_url, stream=True)
print(r.headers['content-length'])
content = r.content
print(len(content))

# stream设置为true无法保证连接被关闭，可以考虑使用with语句
with requests.get('http://httpbin.org/get', stream=True) as r:
    pass

