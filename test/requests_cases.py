import requests

url = 'http://localhost:8080/schedule/task/delete'

params = {
    'authId': '4ED5D140882CD5BA2116C3020C8AB530',
    'targetVolume': 'app_20160726094256',
    'applyType': '0',
    'ids': 'b6219c62-19f4-493c-8',
}

r = requests.get(url, params=params)
print(r.status_code)
print(r.json())
