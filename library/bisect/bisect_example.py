'''
最小堆
'''

import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New Pos Contents')
print('--- --- --------')

l = []
for i in values:
    # 获得i将要被插入的位置
    position = bisect.bisect(l, i)
    # 实际的插入操作
    bisect.insort(l, i)
    print('{:3} {:3}'.format(i, position), l)
