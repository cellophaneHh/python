'''
收到信号时调用处理器进行处理
'''

import signal
import os
import time


def receive_signal(signum, stack):
    print('Received: ', signum)


# 注册signal handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print('My PID is: ', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)
