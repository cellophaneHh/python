from multiprocessing import Process
import time


def f(name):
    print('hello', name)
    time.sleep(30)


if __name__ == '__main__':
    p = Process(target=f, args=('bob', ))
    p.start()
    p.join()
    # 延时结束方便控制台看进程
    time.sleep(60)
