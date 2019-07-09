import pandas as p
d
import numpy as np
import string

# 带索引的数组
s1 = pd.Series(np.arange(10))
print(s1)

# 为数组指定索引
s2 = pd.Series(np.arange(10), index=list('abcdefghij'))
print(s2)

# 通过字典创建Series, 字典的键就是索引，字典的值就是值
s3 = pd.Series({'name': 'xiaoming', 'age': 20})
print(s3)

s4 = {string.ascii_uppercase[i]: i for i in range(10)}
print(type(s4))
print(s4)

# 字典指定索引，如果和key不一致，值是NAN
s4_series = pd.Series(s4, index=list(string.ascii_uppercase[5:15]))
print(s4_series)

# 修改Series的dtype
s5 = pd.Series(np.arange(10), index=list('abcdefghij'))
print(s5)
print(s5.dtype)
s5.astype(float)
print(s5.dtype)

# 取值
s6 = pd.Series(np.arange(10), index=list('abcdefghij'))
print(s6[1])  # 首行
print(s6[[2, 5, 8]])  # 不连续的多行
print(s6[:2])  # 连续的多行(前两行)

# 布尔索引
print(s6[s6 < 5])

# 取index和value
print(s6.index)
print(type(s6.index))
print(s6.values)  # numpy.ndarray
print(type(s6.values))
for index in s6.index:
    print(s6[index])
