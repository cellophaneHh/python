import threading
import time

print()
lock = threading.Lock()

def work():
    lock.acquire()
    print('线程: {}'.format(threading.current_thread().name))
    time.sleep(2)
    lock.release()

t1 = threading.Thread(target=work, name='work1')
t1.start()

t2 = threading.Thread(target=work, name='work2')
t2.start()

t1.join()
t2.join()
