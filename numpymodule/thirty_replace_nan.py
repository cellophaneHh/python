'''
nan值替换为均值
'''
import numpy as np

t1 = np.arange(24).reshape(3, 8).astype(float)
t1[1, 2:] = np.nan
print(t1)

print(np.count_nonzero(np.isnan(t1)))

for i in range(t1.shape[1]):
    temp_col = t1[:, i]  # 第i列
    nan_num = np.count_nonzero(temp_col != temp_col)
    if nan_num != 0:  # 说明有nan
        temp_col_not_zero = temp_col[temp_col == temp_col]
        mean = np.mean(temp_col_not_zero)
        # 将所有为nan的值复制为此列的平均值
        temp_col[np.isnan(temp_col)] = mean

print(t1)
