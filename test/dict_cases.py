# coding: utf-8
"""
字典
"""
my_dict = dict()

my_dict['key'] = 'value'
print(my_dict)

my_dict.pop('key')
print(my_dict)

my_dict['key'] = 'value'
for item in my_dict.items():
    print(item[0], item[1])

my_dict['key1'] = 'value'
my_dict['key0'] = 'value'
print(my_dict)
my_dict.popitem()
print(my_dict)
print(my_dict.keys())

dict_1 = {'a': 'a', 'c': 'c', 'b': 'b'}
print(dict_1)
