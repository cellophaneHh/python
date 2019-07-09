'''
nan值
'''
import numpy as np

t1 = np.nan
t2 = np.nan
print('查看两个nan值是否相等')
print('t1 == t2: {}'.format(t1 == t2))

t3 = np.arange(24).reshape(3, 8).astype(float)
t3[2, 3] = np.nan
t3[2, 4] = np.nan
print(t3)

print("查找数组中所有为nan的值")
print('t3 != t3: {}'.format(t3[t3 != t3]))
print(np.isnan(t3))
print("查找数组中不是0的个数")
print(np.count_nonzero(t3))
print('替换nan为0')
t3[np.isnan(t3)] = 0
print(t3)

print("计算所有的和")
print(np.sum(t3))
print("计算每一列的和")
print(np.sum(t3, axis=0))
print("计算每一行的和")
print(np.sum(t3, axis=1))

print('平均值')
print(np.average(t3, axis=0))

print("中值")
print(np.median(t3))

print("最大值")
print(np.max(t3))
print("均值")
print(np.mean(t3))
print('标准差')
print(np.std(t3))
print("极值，最大值和最小值之差")
print(np.ptp(t3))
