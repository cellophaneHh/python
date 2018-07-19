'''
保证获取时间时是单调增加的，不会出现time()中认为调整服务器时间造成后面获取的时间比前面获取的靠前的问题
'''
import time

start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print('start : {:>9.2f}'.format(start))
print('end : {:>9.2f}'.format(end))
print('span : {:>9.2f}'.format(end - start))
