'''
DataFrame 二维数组
既有行索引，又有列索引
行索引，表明不同行，横向索引，叫做index， 0轴，axis=0
列索引，表明不同列，纵向索引，叫做columns，1轴，axis=1
'''
import pandas as pd
import numpy as np

print()
d1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(d1)

# 修改行索引和列索引
print()
d2 = pd.DataFrame(np.arange(12).reshape(3, 4),
                  index=[1, 2, 3],
                  columns=[1, 2, 3, 4])
print(d2)

print()
# 字典
dic = {'name': 'xiaoming', 'age': 20, 'address': [2, 3], 'tel': [2, 3]}
d3 = pd.DataFrame(dic)
print(type(d3))
print(d3)

# 行列索引
print()
d4 = pd.DataFrame(np.arange(12).reshape((3, 4)),
                  index=list('abc'),
                  columns=list('WXYZ'))
print(d4)
