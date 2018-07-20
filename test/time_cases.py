import time


print(time.clock())

print(time.clock())

print(time.ctime())
print(time.localtime())
print(time.time())

s = time.strptime(time.time())
print(s.tm_m)
