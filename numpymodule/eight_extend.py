'''
数组的拼接
'''
import numpy as np

t1 = np.arange(24).reshape(4, 6)
print('t1=\n{}'.format(t1))

t2 = np.arange(24, 48).reshape(4, 6)
print('t2=\n{}'.format(t2))

print('*' * 10)
print('将两个数组进行垂直拼接')
print(np.vstack((t1, t2)))
print('*' * 10)
print('将两个数组进行水平拼接')
print(np.hstack((t1, t2)))
