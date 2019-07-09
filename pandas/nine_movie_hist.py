'''
绘制电影数据分布
直方图
'''
import pandas as pd
import matplotlib.pyplot as plt

filePath = "./movie.csv"

d1 = pd.read_csv(filePath)

print(d1.head(1))
print(d1.info())

time_data = d1['rating']

max_time = time_data.max()
min_time = time_data.min()

# 会出现除不尽的情况
num_bins = int((max_time - min_time) // 1)
_x = list(range(int(min_time), int(max_time * 2) + 2))
_x = [i / 2 for i in _x]
plt.figure(figsize=(14, 8))
plt.hist(time_data, num_bins)
plt.xticks(_x)

plt.show()
