"""
修改ChainMap中字典的顺序
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print(m.maps)
# 默认按顺序搜索，这里显示的是a中的值
print('c = {}\n'.format(m['c']))

# 翻转存储map的list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}\n'.format(m['c']))
