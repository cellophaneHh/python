import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(
    fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')

file_path = './data1.csv'
data = pd.read_csv(file_path)

# 按value排序，按desc显示前10个
d1 = data.groupby(by='desc').count()['value'].sort_values(ascending=False)[:8]
print(d1)

_x = d1.index
_y = d1.values

plt.figure(figsize=(13, 8))
# plt.bar(_x, _y)
plt.barh(_x, _y)
plt.yticks(_x, ['一', '二', '三', '四', '五', '六'], fontProperties=my_font)
plt.show()
