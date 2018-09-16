import numpy as np

# 传建一个长度为10的数组, 数组值全都是0
array = np.zeros(10, dtype=int)
print(array)

# 传建一个3x5的浮点型数组,数组的值都是1
array = np.ones((3, 5), dtype=float)
print(array)

# 创建一个数组,从0开始,20结束,步长为2
array = np.arange(0, 20, 2)
print(array)

# 创建有5个元素的数组,这5个数均匀分配在0-1
array = np.linspace(0, 1, 5)
print(array)

# ~~~
# 创建一个3x3、均值为0、方差为1的正态分布的随机数数组
array = np.random.normal(0, 1, (3, 3))
print(array)

# 创建一个3x3、[0,10]区间的随机整型数组
array = np.random.randint(0, 10, (3, 3))
print(array)

# 创建一个3x3的单位矩阵
array = np.eye(3)
print(array)

# 创建一个由3个整型数组成的未初始化的数组，数组的值是内存空间中的任意值
array = np.empty(3)
print(array)
