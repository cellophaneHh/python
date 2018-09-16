'''
matlab风格借口位于pyplot中
'''
import matplotlib.pyplot as plt
import numpy as np


# 数据
x = np.linspace(0, 10, 100)

# 画布
plt.figure()

# 创建一个子图
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))

# 创建第二个子图
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

plt.show()
# plt.savefig()
