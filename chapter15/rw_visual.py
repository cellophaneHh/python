import matplotlib.pyplot as plt

from random_walk import RandomWalk

#传进一个RandomWalk实例，并将其包含的点都绘制出来

rw = RandomWalk(10000)
rw.fill_walk()



#绘制起点
plt.scatter(rw.x_values[0], rw.y_values[0], s=100, edgecolors='none', c='green')
#绘制终点
#这个看到有次绘制了两次终点，，还不是一个点???
#貌似是两张图叠一起了。。。。
plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, edgecolors='none', c='red')
point_numbers = list(range(rw.num_points))
print("终点:(" + str(rw.x_values[-1]) + "," + str(rw.y_values[-1]) + ")")
plt.scatter(rw.x_values, rw.y_values, s=10, edgecolors='none', c=point_numbers, cmap=plt.cm.Blues)
#plt.scatter(rw.x_values, rw.y_values, s=10, edgecolors='none', c='red')

plt.title("Random Walk")

#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

#这个和讲的不太一样啊。。。。
#plt.figure(figsize=(10, 6))

plt.show()

# while True:
#     rw = RandomWalk(10000)
#     rw.fill_walk()

#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values, s=10, edgecolors='none', c=point_numbers, cmap=plt.cm.cool)

#     plt.title("Random Walk")

#     plt.show()

#     keep_running = input("keep running?(y/n): ")
#     if keep_running == 'n':
#         break
