import requests
import json
import collections


def show_ids(item):
    dd = collections.defaultdict()
    for k, v in item.items():
        dd[k] = v
    dd.setdefault('children', [])
    print(dd['id'])
    children = dd['children']
    if children:
        for child in children:
            show_ids(child)


url = 'http://localhost:8080/HappyServer/schedule/task/calculateValueTree'

params = {
    'authId': '0B9DC610927A2978E69C51951EA19BA6',
    'targetVolume': 'srfx',
    'parentId': 'htwv',
    'selectedIds': 'cb3127c4-154b-4c59-a,5aedff02-958d-4465-9'
}
json_dumps = json.dumps(params)
print(type(json_dumps))

r = requests.post(url, data=json_dumps, headers={'content-type': 'application/json;charset=utf-8'})
if r.status_code == 200:
    json_result = json.loads(r.text)
    print(json_result)
    item_ids = json_result['items']
    for item_id in item_ids:
        show_ids(item_id)
else:
    print("status_code: {}, reason: {}".format(r.status_code, r.reason))

