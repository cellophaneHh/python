'''
直方图只能绘制未统计的数据
可以通过条形图对统计过的数据进行绘制
'''
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 统计过的数据，但是越往后面组距越大，和普通直方图组距相等不同
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

plt.figure(figsize=(14, 9))
_width = 1
plt.bar(range(len(interval)), quantity, width=1)
# 因为quantity总共有12个，而interval是间隔，总共应该13个才能将quantity显示全
_x = [i - _width / 2 for i in range(len(interval) + 1)]
print(_x)
_x_labels = interval + [150]
plt.xticks(_x, _x_labels)

plt.grid()
plt.show()
