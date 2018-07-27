import requests

url = 'http://localhost:8080/HappyServer/schedule/task/calculateValueTree'

params = {
    'authId': 'B80CA686AA5E21E1ABD1A518A521B4B4',
    'targetVolume': 'YYGL',
    # 'applyType': '8',
    # 'parentId': 'DISPATCH_TASK',
    # 'fileTypes': '-',
    # 'resultType': 'json'
}

r = requests.get(url, params=params)
if r.status_code == 200:
    print(r.text)
else:
    print("status_code: {}, reason: {}".format(r.status_code, r.reason))
