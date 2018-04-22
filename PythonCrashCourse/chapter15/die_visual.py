import pygal

from die import Die

#创建一个D6（6面的）
die = Die()

#掷几次骰子，将结果存放在一个列表中

results = []
for rool_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)
# print(len(results))


#分析每个结果出现的次数
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 绘制直方图，对结果进行可视化
hist = pygal.Bar()

#没提示啊没提示。。。
hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
