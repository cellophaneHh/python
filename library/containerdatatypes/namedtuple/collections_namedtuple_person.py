'''
命名元组
'''

import collections

# 第一个参数是元组名，第二个参数是元组元素的名称，空格分割
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29)
print('\nField by name:', jane.name)

print('\nFields by index:')
for p in [bob, jane]:
    print(*p)
    print('{} is {} years old'.format(*p))
