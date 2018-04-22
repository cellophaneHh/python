import matplotlib.pyplot as plt

from die import Die


count = 100
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

frequencies = [results.count(v) for v in range(1, len(results) + 1)]

print(len(results))
print(len(frequencies))

#matplotlib直方图
#...
