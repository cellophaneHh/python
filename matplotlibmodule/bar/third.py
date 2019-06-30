"""
绘制多次条形图
"""
from matplotlib import font_manager
import matplotlib.pyplot as plt

my_font = font_manager.FontProperties(
    fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')

y_2 = [
    11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17,
    20, 14, 15, 15, 15, 19, 21, 22, 22
]
y_3 = [
    11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17,
    20, 14, 15, 15, 15, 19, 21, 22, 22
]

bar_width = 0.4

x_1 = range(1, len(y_2) + 1)
x_2 = [i + bar_width for i in x_1]
x_3 = [i + bar_width * 2 for i in x_2]

plt.figure(figsize=(14, 8), dpi=80)
# 横着
plt.bar(x_1, y_2, label='february', width=bar_width)
plt.bar(x_2, y_3, label='march', width=bar_width)

plt.grid(alpha=0.2)

plt.legend()

plt.show()
