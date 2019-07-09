'''
交换数组的行或者列
'''
import numpy as np

t1 = np.arange(24).reshape(4, 6)
print('t1=\n{}'.format(t1))

t2 = np.arange(24, 48).reshape(4, 6)
print('t2=\n{}'.format(t2))

# [0, 1]是选中的行的索引
print("交换行, 交换第0行和第1行")
t1[[0, 1], :] = t1[[1, 0], :]
print(t1)

print("交换列, 交换第0列和第1列")
t1[:, [0, 1]] = t1[:, [1, 0]]
print(t1)
