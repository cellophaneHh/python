'''
数组合并join, 按照列索引
'''
import numpy as np
import pandas as pd

print()
d1 = pd.DataFrame(np.ones((2, 4)), index=["A", 'B'], columns=list("abce"))
print(d1)
print('*' * 10)
d2 = pd.DataFrame(np.zeros((3, 3)), index=["A", 'B', "C"], columns=list("xyz"))
print(d2)
print('*' * 10)
print(d1.join(d2))
print('*' * 10)
print(d2.join(d1))
