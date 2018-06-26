import threading
import time

b = threading.Barrier(2, timeout=5)


class MyThread(threading.Thread):

    max_loop = 30

    def __init__(self, t):
        threading.Thread.__init__(self)
        self.t = t

    def run(self):
        self.sleep()

    def sleep(self):
        loop = 1
        while True and loop < 30:
            loop += 1
            print(threading.current_thread().getName() + ', 一次循环')
            time.sleep(self.t)
            print(threading.current_thread().getName() + ", 开始等待")
            b.wait(timeout=5)


t1 = MyThread(1)
t2 = MyThread(2)

t1.start()
t2.start()

t1.join()
t2.join()
