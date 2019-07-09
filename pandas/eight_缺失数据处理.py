'''
pandas 中缺失数据处理
1. 元素为nan
2. 元素为某个特定的值，比如0
'''
import pandas as pd
import numpy as np

d1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
d1.iloc[[0, 2], [3, 1]] = np.nan
print(d1)

print('*' * 10)
print(pd.isnull(d1))
print('*' * 10)
print(pd.notnull(d1))
print('*' * 10)
print(d1[pd.notnull(d1.loc[2, :])])
print('*' * 10)
# 选取第1列不是nan的行
print(d1[pd.notnull(d1[1])])
print('*' * 10)
# 删除存在nan的行
print(d1.dropna(axis=0))
print('*' * 10)
# 删除存在nan的列
print(d1.dropna(axis=1))
print('*' * 10)
# dropna的how参数,按条件删除
print(d1.dropna(axis=0, how='all'))
print('*' * 10)
print(d1.dropna(axis=0, how='any'))
print('*' * 10)
# dropna的inplace参数, 对满足条件的行进行删除操作，会修改d1
d1.dropna(axis=0, how='any', inplace=True)
print('*' * 10)
print(d1)

print('*' * 10)
d1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
d1.iloc[[0, 2], [3, 1]] = np.nan
d1.iloc[[1], [3]] = 0
print(d1)
# 自动将无效数据进行填充，包括0和nan
print(d1.fillna(0))
print(d1.fillna(d1.mean()))
