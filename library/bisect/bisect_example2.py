import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]
print()
print('New Pos Contents')
print('--- --- --------')

l = []
for i in values:
    # 和bitsect最终顺序一直，不同在于相同元素时插在了左边
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}'.format(i, position), l)
