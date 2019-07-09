'''
numpy中的数组裁剪 clip(min, max)
将数组中小于min的赋值为min，大于max的赋值为max
就是将数组的元素限制在区间[min, max]
'''
import numpy as np

t1 = np.arange(24).reshape(4, 6)
print(t1)
t2 = t1.astype(float)
t2[3, 3] = np.nan
print(t2)
# 对数组进行裁剪, 小于3的赋值为3，大于5的赋值为5
print(t2.clip(3, 5))
