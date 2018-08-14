'''
产生指定范围的随机数
这个源码好厉害，关键是想法。。。
'''
import random

for i in range(5):
    print('%04.3f' % random.uniform(1, 100), end=' ')
print()
