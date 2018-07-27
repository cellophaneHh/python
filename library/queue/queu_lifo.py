'''
后进先出队列
'''

import queue

q = queue.LifoQueue()

for i in range(5):
    q.put(i)
print(q.qsize())
while not q.empty():
    print(q.get(), end=" ")
print()
