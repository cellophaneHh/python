import matplotlib.pyplot as plt

from random_walk import RandomWalk

#传进一个RandomWalk实例，并将其包含的点都绘制出来

rw = RandomWalk(1000)
rw.fill_walk()



#绘制折线图
plt.plot(rw.x_values, rw.y_values, linewidth=1)

plt.title("Random Walk")

#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)


plt.show()
