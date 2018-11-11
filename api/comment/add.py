import requests

url = "http://localhost:8080/web/comment/save.do"

data = {
    "content": "评论评论3",
    "type": 1,
    "postId": "632D1427A7EB481394F68EE485601C0F",
    "commentId": "6BC8F33A59E040EB90BCB8196C66FCD6",
    "creatorId": "5591637E84FB4D73BFF3ABF703B0B3A2"
}

res = requests.post(url, data=data)

print(res.status_code)
if res.status_code == 200:
    print(res.text)
else:
    print(res.text)
