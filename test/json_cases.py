import json

json_str = '{"items":[{"checked":false,"children":[{"checked":false,"children":[{"checked":false,"description":"11","id":"11","leaf":false,"open":false,"parentId":"1","text":"11"},{"checked":false,"children":[{"checked":false,"description":"121","id":"121","leaf":true,"open":false,"parentId":"12","text":"121"},{"checked":true,"description":"122","id":"122","leaf":true,"open":false,"parentId":"12","text":"122"}],"description":"12","id":"12","leaf":false,"open":true,"parentId":"1","text":"12"}],"description":"1","id":"1","leaf":false,"open":true,"parentId":"0","text":"1"},{"checked":false,"children":[{"checked":false,"description":"21","id":"21","leaf":false,"open":false,"parentId":"2","text":"21"},{"checked":true,"description":"22","id":"22","leaf":false,"open":false,"parentId":"2","text":"22"}],"description":"2","id":"2","leaf":false,"open":true,"parentId":"0","text":"2"},{"checked":false,"description":"3","id":"3","leaf":false,"open":false,"parentId":"0","text":"3"}],"description":"0","id":"0","leaf":false,"open":true,"parentId":"root","text":"0"}],"success":true}'

print(type(json.loads(json_str)))

mydict = {'1': '中文'}
# 默认中文会编码
with open('test_zh.json', 'w') as f:
    json.dump(mydict, f)

# 加入ensure_ascii=False参数，可显示中文
with open('test_zh.json', 'w') as f:
    json.dump(mydict, f, ensure_ascii=False)
