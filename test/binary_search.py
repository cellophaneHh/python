import numpy as np
import sys
sys.path.append('..')
from algorithm.Merge import Merge


def binary_search_region(datas, data, start, end):
    '''从datas找到data，返回索引'''
    low = start
    hi = end
    while low <= hi:
        mid = (low + hi) // 2
        if datas[mid] > data:
            hi = mid - 1
        elif datas[mid] < data:
            low = mid + 1
        else:
            return mid
    return -1


def binary_search(datas, data):
    return binary_search_region(datas, data, 0, len(datas) - 1)


datas = np.arange(0, 100000, 2, dtype='int')
# Merge.sort(datas)
print(datas[0:10])
data = datas[9]
print(binary_search(datas, data))
