"""
使用pygal绘制散点图
没找到颜色变换的。。。
"""
import pygal

from random_walk import RandomWalk

#传进一个RandomWalk实例，并将其包含的点都绘制出来

rw = RandomWalk(1000)
rw.fill_walk()

#pygal 绘制散点图
xy_chart = pygal.XY(stroke=False)
xy_chart.title = "Random Walk"

xy_data_first = [(rw.x_values[0], rw.y_values[0])]
xy_data_last = [(rw.x_values[-1], rw.y_values[-1])]
xy_data = [(rw.x_values[i], rw.y_values[i]) for i in range(1, len(rw.x_values))]

xy_chart.add('出发点', xy_data_first)
xy_chart.add('其他', xy_data)
xy_chart.add('终止点', xy_data_last)

xy_chart.render_to_file('xy_data.svg')

