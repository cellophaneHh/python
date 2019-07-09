"""
numpy 实现矩阵转置
三种方法
"""
import numpy as np

t1 = np.arange(24).reshape(4, 6)
print('t1 = \n{}'.format(t1))

t2 = t1.transpose()
print('t2 = \n{}'.format(t2))

t3 = t1.T
print('t3 = \n{}'.format(t3))

t4 = t1.swapaxes(1, 0)
print('t4 = \n{}'.format(t4))
