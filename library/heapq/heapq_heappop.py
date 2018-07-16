import heapq
from heapq_heapdata import data

print('random: ', data)
heapq.heapify(data)
print('heapified:')
print(data)
print()

for i in range(2):
    smallest = heapq.heappop(data)
    print('pop {:>3}:'.format(smallest))
    print(data)
