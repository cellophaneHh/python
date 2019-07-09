'''
pandas读取外部数据
'''
import pandas as pd
import numpy as np

# 读取csv文件
datas = pd.read_csv('../numpymodule/data.csv')
print(datas)
