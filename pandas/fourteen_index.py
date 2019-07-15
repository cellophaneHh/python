'''
pandas索引
'''
import pandas as pd
import numpy as np

file_path = "./data1.csv"

df = pd.read_csv(file_path)

# groupby方法对数据进行分组
grouped = df.groupby(by='name')
print(grouped)

value_count = grouped['value'].count()
print(type(value_count))
print(value_count.index)

multiindex = df.groupby(by=['name', 'desc']).count().index
print(multiindex)

d1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(d1)

print(d1.index)
d1.index = ['a', 'b', 'c']
print(d1.index)
# 取原dataframe中指定索引的数据， 不存在的设置为nan
result = d1.reindex(list('de'))
print(result.index)
print(result)
# 指定某一列作为索引
d1.columns = list('abcd')
print()
print(d1.set_index('a'))
print(d1.set_index('a', drop=False))

# 设置两个索引
print()
print(d1.set_index(['a', 'b']))
