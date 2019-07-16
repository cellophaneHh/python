'''
时间序列
'''
import pandas as pd
import numpy as np

# start 开始，end结束，freq频率
dates = pd.date_range(start='20190601', end='20190820', freq='D')
print(dates)

dates10D = pd.date_range(start='20190601', end='20190820', freq='10D')
print(dates10D)
# start 开始，periods个数，freq频率
dates10D = pd.date_range(start='20190601', periods=80, freq='D')
print(dates10D)

datesM = pd.date_range(start='20190601', end='20190820', freq='M')
print(datesM)

print('*' * 10)
index = pd.date_range('20190701', periods=10)
df = pd.DataFrame(np.random.rand(10), index=index)
print(df)
