'''
修改数组的值
'''
import numpy as np

t1 = np.arange(24).reshape(4, 6)
print(t1)

# 获取小于10的内容
print('*' * 10)
print(t1[t1 < 10])
print('*' * 10)
# 将t1中小于10的值赋值3
t1[t1 < 10] = 3
print(t1)

# 使用where进行三元运算
# 将t1中<10的替换为0，其他的替换为10
t2 = np.where(t1 < 10, 0, 10)
print('t2 = \n{}'.format(t2))
