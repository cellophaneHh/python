'''
dataframe描述信息
'''
import pandas as pd
import numpy as np

d1 = pd.DataFrame(np.arange(12).reshape((3, 4)),
                  index=list('abc'),
                  columns=list('WXYZ'))
print()
print(d1)
print('index...')
print(d1.index)
print('columns')
print(d1.columns)
print('values...')
print(d1.values)
print('shape...')
print(d1.shape)
print('dtypes..')
print(d1.dtypes)

# 显示前几行
print("显示前几行")
print(d1.head(2))

# 显示后几行
print('显示后几行')
print(d1.tail(2))

# 概览
print("概览,describe")
print(d1.describe())
print('info...')
print(d1.info())
