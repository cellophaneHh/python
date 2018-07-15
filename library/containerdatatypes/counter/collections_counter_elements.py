import collections

c = collections.Counter('extremely')
c['z'] = 0
print(c)
# elements不会打印出出现个数为0的值
print(list(c.elements()))
