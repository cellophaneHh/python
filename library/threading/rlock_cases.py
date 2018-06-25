import threading

# my_lock = threading.Lock() 换为可重入锁
my_lock = threading.RLock()


class MyThread(threading.Thread):

    def run(self):
        self.show_recursion(1)

    def show_recursion(self, level):
        """
        证明这个锁是不可重入的，即使是同一个线程多次进入
        """
        if level > 100:
            return
        print("线程:" + threading.current_thread().getName() + ", 尝试获得锁..")
        mutex = my_lock.acquire(timeout=5)
        if not mutex:
            print("线程:" + threading.current_thread().getName() + ", 尝试获得锁失败..")
            return
        level = level + 1
        print("线程:" + threading.current_thread().getName() + ", 获得锁..")
        try:
            print("递归调用: " + str(level))
            self.show_recursion(level)
        finally:
            print("线程:" + threading.current_thread().getName() + ", 释放锁..")
            my_lock.release()


t = MyThread()
t.setName('t')

t.start()
t.join()

print("t end....")
