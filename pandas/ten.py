'''

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print()
d1 = pd.read_csv('./random_str.csv')
actors = d1['actor'].str.split(',')
print(actors)
print()

columns_data = []
for i in range(actors.shape[0]):
    columns_data.extend(actors[i])
columns_data = list(set(columns_data))

temp_data = pd.DataFrame(np.zeros((actors.shape[0], len(columns_data))),
                         columns=columns_data)
print(temp_data)
print("*" * 10)
for i in range(actors.shape[0]):
    temp_data.loc[i, actors[i]] = 1

print(temp_data)
sum_data = temp_data.sum(axis=0)
sum_data = sum_data.sort_values()

_x = sum_data.index
_y = sum_data.values

plt.figure(figsize=(14, 8))
plt.bar(range(len(_x)), _y, width=0.6, color='orange')
plt.xticks(range(len(_x)), _x)
plt.grid(alpha=0.2)
plt.show()
