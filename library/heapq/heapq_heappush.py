import heapq
from heapq_heapdata import data

heap = []
print('random: ', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    print(heap)
