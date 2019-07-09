import numpy as np

# 创建数组
a = np.array([[1, 3, 4, 5], [4, 5, 6, 1]])
print(type(a))
print(a)

# 查看数组的形状，返回一个元组，元组的长度是数组的维度,元素是每个维度的元素个数
print(a.shape)

t2 = np.array([1, 2, 3, 4, 5, 6, 7])
print(type(t2))
print(t2)
print(t2.shape)

t4 = np.arange(12)
print('t4', end='=')
print(t4)

# 修改数组的形状, reshape 中参数必须能完全平分原数组元素，否则报错
t5 = t4.reshape((3, 4))
print("t4 reshape", end='= ')
print(t5)

t6 = t4.reshape((2, 2, 3))
print('t4 reshape', end='= ')
print(t6)

# 多维变成一维数组
t7 = t6.reshape((12, ))
print('t7', end='= ')
print(t7)
# 多维变成一维数组的简便方法
t7 = t6.flatten()
print('t7', end='= ')
print(t7)

# 数组和数字运算
print('t5 = {}'.format(t5))
print('t5 + 2 = {}'.format(t5 + 2))
print('t5 / 2 = {}'.format(t5 / 2))
print('t5 * 2 = {}'.format(t5 * 2))
print('t5 - 2 = {}'.format(t5 - 2))
