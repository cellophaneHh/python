'''
类型编码之后在解码可能得不到原来的类型
'''
import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

data_string = json.dumps(data)
print('ENCODED: ', data_string)

decoded = json.loads(data_string)
print('DECODED: ', decoded)

# 之前的元组转换后变为list了
print('ORIGINAL: ', type(data[0]['b']))
print('DECODED: ', type(decoded[0]['b']))
