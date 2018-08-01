import threading
import logging
import queue
import random
import time


def binary_search(key, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        print('before: low: {}, high: {}'.format(low, high))
        mid = round((low + high) / 2)
        print(mid)
        mid_num = nums[mid]
        if mid_num == key:
            return mid
        elif mid_num > key:
            high = mid - 1
        else:
            low = mid + 1
        print('after: low: {}, high: {}'.format(low, high))
    return -1

# 单线程100此randint
start = time.time()
for i in range(100):
    x = [random.randint(1, 100000) for yi in range(10000)]
end = time.time()
print('单线程消耗时间: {}'.format(str(end - start)))


# 多线程任务
def work():
    '''线程任务'''
    for i in range(50):
        x = [random.randint(1, 100000) for yi in range(10000)]

start = time.time()
for i in range(2):
    t = threading.Thread(name=str(i), target=work)
    t.start()

end = time.time()
time.sleep(5)
print('多线程消耗时间: {}'.format(str(end - start)))
