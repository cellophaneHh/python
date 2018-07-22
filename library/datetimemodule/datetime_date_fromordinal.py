import datetime
import time

o = 733114
print('d: ', o)
print('fromordinal(0): ', datetime.date.fromordinal(o))

t = time.time()
print('t: ', t)
print('fromtimestamp(t): ', datetime.date.fromtimestamp(t))
print(datetime.datetime.fromtimestamp(time.time()))
