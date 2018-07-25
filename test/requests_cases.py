import requests

url = 'http://localhost:8080/HappyServer/schedule/task/listAll'

params = {
    'authId': '9742D34D2A3B743A70C9D64EA60605B7',
    'targetVolume': 'YYGL',
    'applyType': '8',
    # 'parentId': 'DISPATCH_TASK',
    # 'fileTypes': '-',
    # 'resultType': 'json'
}

r = requests.get(url, params=params)
if r.status_code == 200:
    print(r.headers['content-type'])
    print(r.text)
else:
    print("status_code: {}, reason: {}".format(r.status_code, r.reason))
