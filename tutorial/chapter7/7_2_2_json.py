# 使用json模块存储结构话数据

import json


s = json.dumps([1, 'simple', 'list'])
print(s)
print(type(s))

with open('json.json', 'w') as f:
    json.dump([1, 'simple', 'list'], f)

with open('json.json', 'r') as f:
    print(json.load(f))

