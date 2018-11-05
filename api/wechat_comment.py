import json
import requests

data = {
    "content": "评论5",
    "type": 1,
    "postId": "asdf",
    "commentId": "0942757A6BC24966A21AE5F37109CFF8",
}

url = "http://localhost:8082/web/comment/save.do"

res = requests.post(url, data=data)

print(res.status_code)
print(res.json())
