# coding: utf-8
"""
为图片设置高级属性，如图片大小，保存到本地，标题，轴描述
"""
from matplotlib import pyplot as plt

x = range(2, 26, 2)

y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 24, 22, 18]

# 设置图片大小
fig = plt.figure(figsize=(20, 8), dpi=80)

# 根据数据绘制图形
plt.plot(x, y)

# 绘制x轴
_xticks = [i / 2 for i in range(4, 49)]
plt.xticks(_xticks)
plt.xlabel("x轴label")

# 绘制y轴
plt.yticks(range(min(y), max(y) + 1))
plt.ylabel("y轴label")
# 保存到本地, 格式自选
# plt.savefig("./second.png")

# 最终展示
plt.show()
