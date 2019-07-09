'''
选择满足某些条件的数据
'''
import pandas as pd
import numpy as np

d1 = pd.read_csv('./data.csv')

print(d1[(d1['value'] > 20) & (d1['value'] < 150)])

# 名字长度大于2
print(d1[d1['name'].str.len() > 2])
