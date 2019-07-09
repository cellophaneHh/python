import numpy as np
import random

t1 = np.arange(4).reshape((4, 1))
print("t1 = {}".format(t1))

t2 = np.arange(12).reshape((4, 3))

print('t2 = {}'.format(t2))

# 列相同
print('t1 + t2 = {}'.format(t1 + t2))
print('t2 + t2 = {}'.format(t2 + t2))

print(t1.dtype)

t4 = np.array(range(1, 4), dtype=bool)
print(t4)
t4.astype('int8')
print(t4)
print(t4.dtype)

# 小数
t5 = np.array([random.random() for i in range(10)])
print(t5)
print(t5.dtype)

# 取小数位数
t6 = np.round(t5, 2)
print("t6 = {}".format(t6))
