import collections

Person = collections.namedtuple('Person', 'name age')

pat = Person(name='Pat', age=12)
print('\nRepresentation:', pat)

# namedtuple和元组一样是不可变的
try:
    pat.age = 21
except AttributeError:
    print('不能更新值')
