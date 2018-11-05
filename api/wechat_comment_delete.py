import json
import requests

data = {
    "commentId": "FF0A536FE8E64AD78781A5BF6F572483",
    "commentType": 0
}

url = "http://localhost:8082/web/comment/delete.do"

res = requests.post(url, data=data)

print(res.status_code)
print(res.json())
