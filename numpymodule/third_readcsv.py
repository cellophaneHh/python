"""
从csv文件中读取文件
"""
import numpy as np

t1 = np.loadtxt('./data.csv', delimiter=',', dtype='int64')
print(t1)

# 转置
t2 = np.loadtxt('./data.csv', delimiter=',', dtype='int64', unpack=True)
print(t2)
