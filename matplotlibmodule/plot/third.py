# coding: utf-8
"""
为图片设置高级属性，如图片大小，保存到本地，标题，轴描述
"""
from matplotlib import font_manager
from matplotlib import pyplot as plt

# 两种修改字体支持中文的方法

## 测试无效, 提示字体不存在
# font = {
#     'family': 'Droid Sans Fallback',
#     'weight': 'regular',
#     'size': 12
# }
# matplotlib.rc("font", **font)

# 使用fontmanager
my_font = font_manager.FontProperties(
    fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')

x = range(2, 26, 2)

y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 24, 22, 18]

# 设置图片大小
fig = plt.figure(figsize=(20, 8), dpi=80)

# 根据数据绘制图形
plt.plot(x, y)

# 绘制x轴
_xticks = [i / 2 for i in range(4, 49)]
_xticks_label = ["hello, {}".format(i) for i in _xticks]
# rotation参数按角度逆时针旋转x轴提示信息，保证不遮挡
plt.xticks(_xticks, _xticks_label, rotation=40)

# 绘制y轴
plt.yticks(range(min(y), max(y) + 1))
# 设置y轴label和中文字体显示
plt.ylabel("y轴label", FontProperties=my_font)

# 标题
plt.title("温度趋势", FontProperties=my_font)
# 保存到本地, 格式自选
# plt.savefig("./second.png")

# 最终展示
plt.show()
