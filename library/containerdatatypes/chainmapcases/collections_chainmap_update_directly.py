"""
可以直接通过chainmap更新原来的map
因为chainmap中存储的是引用
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: ', m)
# 只会更新chanmap中存在c的map
m['c'] = 'E'
print('After: ', m)
print('a:', a)
