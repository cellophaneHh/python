"""
从csv文件中读取最后一列绘制直方图
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(
    fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')

t1 = np.loadtxt('./data.csv', delimiter=',', dtype='int64')

# 选择最后一列比500小的数据
t1 = t1[t1[:, -1] < 100]

t2 = t1[:, -1]
t3 = t1[:, 1]

plt.figure(figsize=(13, 7))
plt.scatter(t2, t3, label='点')
plt.legend(prop=my_font, loc='upper right')
plt.show()
