'''
格式可读
可通过参数实现键排序、缩进等
'''
import json

data = [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
print('DATA:', repr(data))


print('repr(data): ', len(repr(data)))

plain_dump = json.dumps(data)
print('dumps(data): ', len(plain_dump))
print(plain_dump)

small_indent = json.dumps(data, indent=2)
print('dumps(data, indent=2): ', len(small_indent))

with_separators = json.dumps(data, separators=(',', ':'))
print('dumps(data, separators): ', len(with_separators))
print(with_separators)
