"""
"""
import requests
import json

# url = 'http://localhost:8081/web/post/add.do'
url = 'http://localhost:8081/web/post/delete.do'
images = ['asdfasdf', "123412342qw34"]
post = {
    "creatorId": "123",
    "circleId": "sqdf",
    "location": "beijing",
    "content": "yigemeihaodezhoumoaaaaa",
    "images": images,
    "link": "http://www.sina.com.cn/",
    "typt": "1"
}

deleteId = {
    "postId": "b63fa54edd9e417d8830a67f9e72d458"
}
r = requests.post(url, data=deleteId)

print(r.text)
print(r.headers)
