'''
将t1和t2合并，并且保留国家信息(增加一列)
'''
import numpy as np

t1 = np.arange(24).reshape(4, 6)
print('t1=\n{}'.format(t1))
t1_c = np.array([0 for i in range(4)]).reshape(4, 1)
print(t1_c)
t1 = np.hstack((t1_c, t1))
print(t1)

t2 = np.arange(24, 48).reshape(4, 6)
print('t2=\n{}'.format(t2))
t2_c = np.array([1 for i in range(4)]).reshape(4, 1)
print(t2_c)
t2 = np.hstack((t2_c, t2))

result = np.vstack((t1, t2))
print(result)
