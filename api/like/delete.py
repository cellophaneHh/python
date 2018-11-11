import requests

url = "http://localhost:8080/web/like/delete.do"

data = {
    "creatorId": "5591637E84FB4D73BFF3ABF703B0B3A2",
    "type": 1,
    "postId": "632D1427A7EB481394F68EE485601C0F",
    "commentId": "CF5405C98BF9470DA36241A6D1B395DA",
}

res = requests.post(url, data=data)

print(res.status_code)
if res.status_code == 200:
    print(res.text)
    with open('./test.json', "w+") as fp:
        fp.writelines(res.text)
else:
    print(res.text)
