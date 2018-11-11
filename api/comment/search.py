import requests

url = "http://localhost:8080/web/comment/search.do"

data = {
    "postId": "632D1427A7EB481394F68EE485601C0F",
}

res = requests.post(url, data=data)

print(res.status_code)
if res.status_code == 200:
    print(type(res.text))
    with open('./test.json', "w+") as fp:
        fp.writelines(res.text)
else:
    print(res.text)
