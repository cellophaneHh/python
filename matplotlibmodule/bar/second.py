"""
绘制横着的条形图
"""
from matplotlib import font_manager
import matplotlib.pyplot as plt

my_font = font_manager.FontProperties(
    fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')

x_2 = [
    11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17,
    20, 14, 15, 15, 15, 19, 21, 22, 22
]

x = range(1, len(x_2) + 1)

plt.figure(figsize=(14, 8), dpi=80)
# 横着
plt.barh(x, x_2, label='february')

plt.grid(alpha=0.2)

plt.legend()

plt.show()
