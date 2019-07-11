'''
pandas中的分组和聚合
'''
import pandas as pd
import numpy as np

file_path = "./data1.csv"

df = pd.read_csv(file_path)

# groupby方法对数据进行分组
# grouped = df.groupby(by=['name', 'desc'])
grouped = df.groupby(by='name')
print(grouped)

for key, data in grouped:
    print(key)
    print(data)
    print(type(data))
    print('*' * 10)

# 统计个数
print(grouped.count())
name_count = grouped['name'].count()
print(name_count)
print(name_count['z1'])
print(name_count['z2'])

# 数据按照多个条件进行分组, series进行groupby
grouped = df['value'].groupby(by=[df['name'], df['desc']])
print(grouped)
for x in grouped:
    print(x)
