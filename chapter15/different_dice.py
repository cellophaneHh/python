import pygal

from die import Die


count = 1000
dies = [Die(), Die()]
num = 1

def roll_all(dies):
    """所有骰子掷一次相加结果"""
    result = 1
    for die in dies:
        result *= die.roll()
    return result

def max_result(dies):
    """最大值"""
    result = 1
    for die in dies:
        result *= die.num_sides
    return result

#掷几次骰子，将结果存放在一个列表中
results = [roll_all(dies) for n in range(count)]

frequencies = [results.count(v) for v in range(num, max_result(dies) + 1)]

#可视化
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and D10 50000 times'
hist.x_labels = [str(x) for x in range(num, max_result(dies) + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add("Die", frequencies)
hist.render_to_file('dice_visual.svg')
