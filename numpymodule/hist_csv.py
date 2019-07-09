"""
从csv文件中读取最后一列绘制直方图
"""
import numpy as np
from matplotlib import pyplot as plt

t1 = np.loadtxt('./data.csv', delimiter=',', dtype='int64')
t2 = t1[:, -1]
print(t2)
t2_max = t2.max()
t2_min = t2.min()
print(t2_max)
print(t2_min)
step = 500
num_bin = (t2_max - t2_min) // step
print(num_bin)

plt.figure(figsize=(13, 8))
plt.hist(t2, num_bin, color='orange')
plt.xticks([i for i in range(t2_min, t2_max + step, step)])
plt.grid()
plt.show()
