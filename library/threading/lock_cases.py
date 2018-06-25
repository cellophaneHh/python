# coding: utf-8

import threading
import time

# 获得一个锁
my_lock = threading.Lock()


def show():
    thread_name = threading.current_thread().getName()
    print("线程:" + thread_name + ", 需要申请锁")
    my_lock.acquire()
    try:
        print("线程: " + thread_name + ", 申请到了锁")
        print(threading.current_thread().getName())
        time.sleep(3)
    except Exception as e:
        print("发生了异常...")
    finally:
        print("线程: " + thread_name + ", 释放锁。。。")
        my_lock.release()


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
    print("线程:" + threading.current_thread().getName() + ", 尝试获得锁..")
    mutex = my_lock.acquire(timeout=5)
    if not mutex:
        print("线程:" + threading.current_thread().getName() + ", 尝试获得锁失败..")
        return
    print("线程:" + threading.current_thread().getName() + ", 获得锁..")
    try:
        print("递归调用.")
        show_recursion()
    finally:
        print("线程:" + threading.current_thread().getName() + ", 释放锁..")
        my_lock.release()


t3 = threading.Thread(name='t3', target=show_recursion)

t3.start()
t3.join()

print("t3 end....")
