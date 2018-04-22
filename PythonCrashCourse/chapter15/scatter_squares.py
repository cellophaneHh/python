"""
利用scatter()绘制散点图
"""
import matplotlib.pyplot as plt

#绘制单个点，只传x和y坐标
# plt.scatter(2, 4, s=200)

#绘制多个点,传x和y坐标的列表
# x_values = [x for x in range(1, 6)]
# y_values = [y**2 for y in range(1, 6)]
# plt.scatter(x_values, y_values, s=200)

#循环生成多个点
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#设置每个点的边缘颜色(默认黑色)
edgecolor='none'

#设置单一颜色
c = 'red' #直接写颜色名称
c = (0, 0.5, 0.8) #rgb

#设置颜色映射
c = y_values
cmap = plt.cm.cool

plt.scatter(x_values, y_values, c=c, cmap=cmap, edgecolor=edgecolor, s=40)

#设置图标标题并给坐标轴加上标签
plt.title('Square Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#显示图表
plt.show()

#保存图表
#plt.savefig('squares_plot.png', bbox_inches='tight')
