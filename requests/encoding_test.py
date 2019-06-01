import requests

headers = {
    "user-agent":
    "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
    "accept-encoding": "gzip, deflate"
}

res = requests.get("https://movie.douban.com/chart", headers=headers)
res.encoding = "utf-8"
print(res.headers)
print(res.text)
