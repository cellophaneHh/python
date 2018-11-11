import requests
import json

url = "http://localhost:8080/web/post/search.do"

data = {
    "circleId": "",
    "distance": 10,
    "longitude": 120.2623954500,
    "latitude": 30.1573316200,
    "min": 0,
    "max": 10,
    "creatorId": "5591637E84FB4D73BFF3ABF703B0B3A2"
}

res = requests.post(url, data=data)

with open("./test.json", "w+") as result:
    result.write(res.text)

if res.status_code != 200:
    print(res.reason())
