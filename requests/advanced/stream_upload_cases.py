"""
流式上传文件，允许上传很大的文件
"""

import requests
# 只需要将文件对象赋值给data
with open('massive-body', 'rb') as f:
    requests.post('http://some.url/streamed', data=f)

# 同时上传多个文件
url = 'http://httpbin.org/post'
multiple_files = [
    ('images', ('foo.png', open('foo.png', 'rb', 'image/png'))),
    ('images', ('bar.png', open('bar.png', 'rb', 'image/png')))
]
r = requests.post(url, files=multiple_files)
print(r.text)
