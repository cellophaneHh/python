'''
从两端添加元素
右侧添加
append, extend
左侧添加
appendleft, extendleft
'''

import collections

# add to the right

d1 = collections.deque()
d1.extend('abcdefg')
print('extend: ', d1)
d1.append('h')
print('append: ', d1)

# add to the left
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)

dd = collections.deque()
print(dd.maxlen)
