import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data2.csv')
print(df)
print(df.info())
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
print(df)
print(df.info())
# 将index设置为时间序列(inplace=True, 将作为索引的列剔除)
# 之后重采样
df.set_index('time', inplace=True)
d1 = df.resample('H').count()['name']

_x = d1.index
_y = d1.values
plt.plot(_x, _y)
plt.xticks(_x, _x, rotation=30)
plt.show()
pd.date_range()
