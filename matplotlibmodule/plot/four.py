# coding: utf-8
'''

'''
from matplotlib import font_manager
import matplotlib.pyplot as plt

my_font = font_manager.FontProperties(
    fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')

y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
x = range(11, 31)
plt.figure(figsize=(14, 8))

plt.plot(x, y)

plt.xticks(x, ["{}岁".format(i) for i in x], FontProperties=my_font)
plt.xlabel("年龄", FontProperties=my_font)
plt.ylabel("女朋友个数", FontProperties=my_font)
plt.title('从11岁到30岁每年交女朋有的数量', FontProperties=my_font)

# 绘制网格
plt.grid(alpha=0.2)

plt.show()
