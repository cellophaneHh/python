'''
地图
'''
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figuree(figsize=(8, 8))
m = Basemap()
m.drawcoastlines()
plt.show()
