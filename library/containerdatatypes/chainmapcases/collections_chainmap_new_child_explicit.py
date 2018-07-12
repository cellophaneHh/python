"""
向chainmap中插入一个已知的map
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
# 将c插入到chainmap中
m2 = m1.new_child(c)

print(m1.maps)
print(m2.maps)

print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))
