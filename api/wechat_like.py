import json
import requests

data = {
    "type": 0,
    "postOrCommentId": "asdf",
    "creatorId": "创建人id",
}

url = "http://localhost:8080/web/like/save.do"

res = requests.post(url, data=data)

print(res.status_code)
print(res.json())
