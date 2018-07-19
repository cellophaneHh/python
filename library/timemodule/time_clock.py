'''
这里用到了__file__这个参数
必须在命令行里运行才能成功
python time_clock.py
'''
import hashlib
import time

print(__file__)
# Data to use to calculate md5 checksums
data = open(__file__, 'rb').read()

for i in range(5):
    h = hashlib.sha1()
    print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
        time.time(), time.clock()))
    for i in range(300000):
        h.update(data)
    cksum = h.digest()
