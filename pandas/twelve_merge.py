'''
数组合并merge，按照行索引
'''
import numpy as np
import pandas as pd

print()
d1 = pd.DataFrame(np.ones((2, 4)), index=["A", 'B'], columns=list("abce"))
print(d1)

d3 = pd.DataFrame(np.zeros((3, 3)), columns=list('fax'))
d3.loc[1, 'a'] = 1
print(d3)

# 默认合并 inner
print(d1.merge(d3, on='a'))

print('*' * 10)
d3 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list('fax'))
print(d3)

# 默认how=inner, 交集
print()
print(d1.merge(d3, on='a'))
d1.loc['A', 'a'] = 0
# 指定合并方式, 默认inner
print()
# outer ，并集
print(d1.merge(d3, on='a', how='outer'))
print()
# left， 左为主, 右边缺失的补nan
print(d1.merge(d3, on='a', how='left'))
print()
# right, 右为主，坐标缺失的补nan
print(d1.merge(d3, on='a', how='right'))
