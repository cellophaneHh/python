'''
ravel方法将数组变成一维数组
'''
import numpy as np

data = np.arange(24).reshape((4, 6))

print(data)

print(data.ravel())
