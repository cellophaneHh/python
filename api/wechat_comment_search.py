import json
import requests

data = {
    "postId": "asdf",
}

url = "http://localhost:8082/web/comment/search.do"

res = requests.post(url, data=data)

print(res.status_code)
print(res.text)
