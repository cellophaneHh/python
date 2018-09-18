'''
格式可读
可通过参数实现键排序、缩进等
'''
import json

data = [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
print('DATA:', repr(data))


print("NORMAL: ", json.dumps(data, sort_keys=True))
print('INDENT: ', json.dumps(data, sort_keys=True, indent=2))
