'''
格式可读
可通过参数实现键排序、缩进等
'''
import json

data = [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
print('DATA:', repr(data))

# 排序
unsorted = json.dumps(data)
print('JSON: ', json.dumps(data))
print('SORT: ', json.dumps(data, sort_keys=True))

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print('UNSORTED MATCH: ', unsorted == first)
print('SORTED MATCH: ', first == second)
