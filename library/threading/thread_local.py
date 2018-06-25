import threading

my_data = threading.local()

t1 = threading.Thread(name='t1', target=lambda: print(threading
                                                      .current_thread()
                                                      .getName()))
t2 = threading.Thread(name='t2', target=lambda: print(threading
                                                      .current_thread()
                                                      .getName()))

t1.start()
t2.start()

t1.join()
t2.join()
print(t1.ident)
print("====结束了....")


class MyThread(threading.Thread):

    def run(self):
        print("自定义线程......")


t3 = MyThread()
t3.start()
t3.join()

print("t3结束了。。。")
