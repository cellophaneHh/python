import matplotlib.pyplot as plt

from random_walk import RandomWalk

#传进一个RandomWalk实例，并将其包含的点都绘制出来

rw = RandomWalk(5000)
rw.fill_walk([1], [1,2,3,4,5,6,7,8], [1,-1])

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s=10, edgecolors='none', c=point_numbers, cmap=plt.cm.Blues)
#plt.scatter(rw.x_values, rw.y_values, s=10, edgecolors='none', c='red')

plt.title("Random Walk")

#隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)


plt.show()
