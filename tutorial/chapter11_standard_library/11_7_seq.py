"""
列表工具
array
"""
from array import array

a = array('H', [4000, 10, 700, 22222])
print(a)
print(type(a))
print(sum(a))
print(a[1:3])

# 双端队列
from collections import deque

d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('Handling', d.popleft())

# 列表

import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

# 堆

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
print(data)
heappush(data, -5)
print(data)
data_tmp = [heappop(data) for i in range(3)]
print(data_tmp)
