# coding: utf-8
'''
同一张图形中绘制两条折线, 并为每条线添加标注
'''
from matplotlib import font_manager
import matplotlib.pyplot as plt

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\STKAITI.TTF')

y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 0, 0, 2, 1, 2, 1, 3, 4, 4, 3, 2, 3, 1, 3, 3, 0, 1, 1]
x = range(11, 31)

# 设置画布大小和背景色
plt.figure(figsize=(9, 6), facecolor="red")

plt.plot(x, y1, label='自己', color='orange', linestyle=':')
plt.plot(x, y2, label='同桌', color='cyan')

plt.xticks(x, ["{}岁".format(i) for i in x], FontProperties=my_font)
plt.xlabel("年龄", FontProperties=my_font)
plt.ylabel("女朋友个数", FontProperties=my_font)
plt.title('从11岁到30岁每年交女朋有的数量', FontProperties=my_font)

# 绘制网格
plt.grid(alpha=0.2)

# 添加图例, 显示每条折线的label, 并设置中文字体
plt.legend(prop=my_font, loc='upper right')

plt.show()
