"""
利用plot()绘制折线图
"""
import matplotlib.pyplot as plt

squares = [x**2 for x in range(1, 6)]

#为plot提供输入值，不提供的话会默认按squares索引作为x轴
input_values = [x for x in range(1,6)]

# plt.plot(squares)
# plt.show()

#可以设置线条宽度
plt.plot(input_values, squares, linewidth=5)

#设置图标标题，并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)


#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
