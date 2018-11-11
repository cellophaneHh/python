'''
images是文件数组
type: 0:文本,1:图片,2:链接,3:文本链接,4:文本图片
'''
import requests
import json

url = "http://localhost:8080:/web/post/save"

# 文本保存
data = {
    "creatorId": "",
    "circleId": "",
    "longitude": "",
    "latitude": "",
    "content": "",
    "link": "",
    "images": "",
    "type": ""
}
