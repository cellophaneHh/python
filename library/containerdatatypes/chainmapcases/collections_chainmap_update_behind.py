"""
更新值

chainmap中只是存储了原map的引用
这样更新原来的map，在chainmap中就可以查到
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After: {}'.format(m['c']))
