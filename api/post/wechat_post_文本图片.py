import requests
import json

url = "http://localhost:8080/web/post/save.do"
form_data = {
    "creatorId": "5591637E84FB4D73BFF3ABF703B0B3A2",
    "circleId": "",
    "location": "杭州萧山区萧山体育馆",
    "longitude": 120.2623354500,
    "latitude": 30.1573396200,
    "content": "测试文本图片",
    "link": None,
    "type": "4"
}
images = [
       ("image", ("shortcut.jpg", open("/home/zh/Pictures/500e503f027c7.jpg", "rb"), "image/jpeg"))
    ]

res = requests.post(url, data=form_data, files=images)

if res.status_code == 200:
    print(res.json())
else:
    print(res.reason)
