'''
产生 0<= x < 1.0的随机数
'''
import random

for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()
