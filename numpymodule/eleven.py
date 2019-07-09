'''
工具方法
'''
import numpy as np

# 获取最大值最小值的位置
t1 = np.arange(24).reshape(3, 8)
print(t1)
print("获取最大值")
print(np.argmax(t1))
print("每一列最大值位置")
print(np.argmax(t1, axis=0))
print("每一行最大值位置")
print(np.argmax(t1, axis=1))

# 创建一个全为0的数组
print("全为0的数组")
print(np.zeros((2, 3)))
print("全为1的数组")
print(np.ones((2, 3)))

# 创建一个对角线为1的正方形数组
print("创建一个对角线为1的正方形数组")
print(np.eye(3))

print("从给定上下限内选取随机整数")
print(np.random.randint(0, 10, (4, 5)))
print("创建d0~dn维度的均匀分布的随机数数组, 浮点数,范围0～1")
print(np.random.rand(10, 2))
print("创建d0-dn维度的标准正态分布随机数, 浮点数, 平均数0, 标准差1")
print(np.random.randn(1, 10))
print("产生具有均匀分布的数组, low起始值, high结束值, size形状")
print(np.random.uniform(1, 10, (4, 5)))
print("从指定正态分布中随机抽取样本, 分布中心是loc(概率分布的均值), 标准差是scale, 形状是size")
print(np.random.normal(0, 0.2, (4, 5)))
print('随机数种子,seed(s) s为种子值，因为计算机生成的是伪随机数，所以通过设定相同的随机数种子，可以每次生成相同的随机数')
# 每次都一样了
for i in range(3):
    np.random.seed(10)
    t = np.random.randint(0, 10, (4, 5))
    print(t)
