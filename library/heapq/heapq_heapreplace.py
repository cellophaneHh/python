import heapq
from heapq_heapdata import data

heapq.heapify(data)
print('start:')
print(data)


for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace {:>2} with {:>2}:'.format(smallest, n))
    print(data)
