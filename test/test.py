'''文本显示动画效果'''
import itertools
import sys
import time

for i in itertools.cycle('|/-\\'):
    msg = i + ' ' + 'thinking'
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(.1)
    # 退格符将内容清除
    sys.stdout.write('\x08' * len(msg))
