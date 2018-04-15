"""
利用matplotlib绘制直方图
"""
import matplotlib.pyplot as plt

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

x_data = [v for v in range(num, max_result(dies) + 1)]
y_data = [results.count(v) for v in x_data]

#可视化
plt.title = 'Results of Rolling Dies'
plt.axis()
plt.bar(x_data, y_data, color='red')

plt.show()
