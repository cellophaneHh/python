# 测试Timer对象
# 延迟interval（单位s）之后执行某一个任务
from threading import Timer
import time


def hello():
    print('hello, world')


t = Timer(interval=3, function=hello)
t.start()

t.join()
