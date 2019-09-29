# coding: utf-8

import threading
import time

# 获得一个锁,不可重入
my_lock = threading.Lock()
# 可重入锁
my_rlock = threading.RLock()
global_lock = threading.Lock()


def show():
    thread_name = threading.current_thread().getName()
    print("thread: " + thread_name + ", need lock")
    global_lock.acquire()
    try:
        print("thread: " + thread_name + ", have lock")
        print(threading.current_thread().getName())
        time.sleep(3)
    except Exception as e:
        print("throw exception...")
    finally:
        print("thread: " + thread_name + ", release lock...")
        global_lock.release()


t1 = threading.Thread(name='t1', target=show)
t2 = threading.Thread(name='t2', target=show)

t1.start()
t2.start()

t1.join()
t2.join()

print("end.....")


# 证明这个锁是不可重入的
def show_recursion():
    """
    证明这个锁是不可重入的，即使是同一个线程多次进入
    """
    print("thread:" + threading.current_thread().getName() + ", need lock..")
    mutex = my_rlock.acquire(timeout=5)
    if not mutex:
        print("thread:" + threading.current_thread().getName() +
              ", acquiring lock..")
        return
    print("thread:" + threading.current_thread().getName() + ", have lock..")
    try:
        print("recursion invoke.")
        show_recursion()
    finally:
        print("thread: " + threading.current_thread().getName() +
              ", release lock..")
        my_rlock.release()


t3 = threading.Thread(name='t3', target=show_recursion)

t3.start()
t3.join()

print("t3 end....")
