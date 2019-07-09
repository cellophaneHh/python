"""
numpy的索引和切片
"""
import numpy as np

t1 = np.loadtxt('./data.csv', delimiter=',', dtype='int64')
print(t1)

# 取行
print('*' * 10)
print(t1[2])

print('*' * 10)
# 取连续多行
print(t1[2:])
print('*' * 10)
# 取不连续多行, t1[行,列]
print(t1[[2, 8, 10]])
print(t1[range(2, 10, 2)])
print("取第二行")
print(t1[1, :])

print('*' * 10)
print("取列, 会将此列单独取出来形成一个一维的数组")
print(t1[:, 0])
print('*' * 10)
print("取连续的多列, 会将原数组中每个子数组中满足的列切出来,还是多维的")
print(t1[:, 2:])
print('*' * 10)
print("取不连续的多列")
print(t1[:, [0, 3, 4]])
print('*' * 10)
print("取行和列")
print(t1[2, 4])
print(type(t1[2, 4]))
print('*' * 10)
print('取多行和多列, 取第二行到第五行，第二列到第四列')
print(t1[1:5, 1:4])
print('*' * 10)
print('取多个不相邻的点, 选取点(0,0),(2, 1)和(3, 4)')
print(t1[[0, 2, 3], [0, 1, 4]])
