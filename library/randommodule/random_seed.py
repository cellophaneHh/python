'''
通过设置种子产生固定的伪随机数
'''
import random

random.seed(1)

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')
print()