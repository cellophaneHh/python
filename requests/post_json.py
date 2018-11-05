"""
传json对象
"""
import requests
import json

url = 'http://localhost:8081/web/post/add.do'
images = ['asdfasdf', "123412342qw34"]
post = {
    "creatorId": "123",
    "circleId": "sqdf",
    "location": "beijing",
    "content": "yigemeihaodezhoumoaaaaa",
    "images": images,
    "link": "http://www.sina.com.cn/",
    "type": 1
}

r = requests.post(url, data=post)

print(r.text)
print(r.headers)
