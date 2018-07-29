'''
Lock是不能被多次获取的，即使是同一个线程
'''
import threading


lock = threading.Lock()

print('First try: ', lock.acquire())
print('Second try: ', lock.acquire(0))


