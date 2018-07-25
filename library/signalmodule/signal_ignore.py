'''
可以使用signal.SIG_IGN处理器忽略一些信号
例如下面忽略signal.SIGINT信号(Ctrl+C)
'''
import signal
import os


def do_exit(sig, stack):
    raise SystemExit('Exiting')


signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('My PID: ', os.getpid())

signal.pause()
