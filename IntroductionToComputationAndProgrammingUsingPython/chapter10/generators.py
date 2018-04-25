import random


def int_generator_asc(max_num, step=1):
    """根据最大值和步长生成自增整数序列"""
    num = 1
    for i in range(max_num):
        yield random.randint(num, num + step)
        num = num + step + 1


def int_generator_random(num, max_num=100):
    """根据最大值生成范围内的一个整数序列"""
    for i in range(num):
        yield random.randint(0, max_num)
