import requests
import json
#
url = 'http://localhost:8080/web/requestBody'
# url = "http://httpbin.org/post"
session = requests.session()
data = {'name': '1', 'address': '2'}
print(type(data))
print(type(json.dumps(data)))
response = session.post(url=url, headers={'content-type': 'application/json;charset=UTF-8'},
                        data=json.dumps(data))
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, end=' ')
    print(response.reason)
print("content-type: {}".format(response.headers['content-type']))


def show(num) -> (int, None):
    print(num)


show(10)
