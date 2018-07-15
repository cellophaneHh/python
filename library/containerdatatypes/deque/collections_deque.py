'''
双端队列
'''

import collections

# 接受一个iterable和最大长度作为初始化参数，这里例子最大长度为8
d = collections.deque('abcdefg', 8)

print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.append('s')
print(d)

# 超过最大长度时，如果从一端添加元素，会丢弃另一端的元素
d.append('h')
print(d)
d.appendleft('i')
print(d)

# 支持__getitem__
print(d.__getitem__(1))
