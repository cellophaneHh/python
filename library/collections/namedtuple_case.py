import collections

a = collections.namedtuple('a', ['name', 'age'])

x = a(name='1', age=2)
print(x)
