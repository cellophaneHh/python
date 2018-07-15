import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nBefore:', bob)

# 由于命名元组是不可变的
# 这个方法实际上是返回了一个新建的对象
bob2 = bob._replace(name='Robert')
print('After:', bob2)
print('Sam?:', bob is bob2)
