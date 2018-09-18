'''
json的键必须是字符串，不是字符串会报错
或者使用skipkeys忽略不是字符串的键
'''
import json

data = [{'a': 'A', 'c': 3.0, 'b': (2, 4), ('d',): 'D tuple'}]
print('DATA:', repr(data))

print('First attempt')
try:
    print(json.dumps(data))
except TypeError as err:
    print('ERROR: ', err)

print()
print('Second attempt')
print(json.dumps(data, skipkeys=True))
