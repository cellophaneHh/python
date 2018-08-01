import queue


queue1 = queue.Queue()

queue1.put(1)
print(queue1.get())

if queue1.qsize() > 0:
    print('2')
