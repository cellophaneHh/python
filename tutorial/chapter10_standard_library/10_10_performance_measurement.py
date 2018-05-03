"""
性能衡量
timeit模块
"""
from timeit import Timer

# 记录执行t=a; a=b; b=t的时间
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b = b,a', 'a=1; b=2').timeit())


"""
使用time记录一段代码执行时间
"""
import time

start = time.clock()
time.sleep(3)
print(time.clock() - start)

