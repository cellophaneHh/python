'''
pandas取行或者取列
'''
import pandas as pd
import numpy as np

d1 = pd.read_csv('./data.csv')

print(d1.index)
print(d1.columns)
print('*' * 10)
print(d1.sort_values(by='value'))

# 前2行, 方括号内写数字, 结果还是dataframe
print(d1[:2])
# 取某一列,方括号内写字符串，列名, 结果是series
print(d1['name'])

print()
# loc, 通过标签索引行数据
d2 = pd.DataFrame(np.arange(12).reshape((3, 4)),
                  index=list('abc'),
                  columns=list('WXYZ'))
print(d2)

print("*" * 10)
# 取某个元素
print(d2.loc['a', 'Z'])
# 某一行的所有列
print(d2.loc['a', :])
# 取某一列
print(d2.loc[:, 'Z'])
# 取某个范围内的行, 此时冒号操作会包含两侧的值, 并且只取某几列
print()
print(d2.loc['a':'b', ['W', 'Z']])

print('*' * 5)
print(d2.iloc[:, 2])
print('*' * 5)
print(d2.iloc[1:2, :])
print('*' * 5)
print(d2.iloc[[0, 2], [1, 2]])
print('*' * 5)
# 赋值
d2.iloc[[0, 2], [1, 2]] = 10
print(d2)
