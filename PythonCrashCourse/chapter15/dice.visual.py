import pygal

from die import Die

#创建一个D6（6面的）
die_1 = Die()
die_2 = Die()

#掷几次骰子，将结果存放在一个列表中

results = []
for rool_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析每个结果出现的次数
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 绘制直方图，对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = [str(x) for x in range(2, max_results + 1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')
