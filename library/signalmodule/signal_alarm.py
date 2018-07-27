'''
隔一段时间后发送信号
'''
import signal
import time


def receive_alarm(signum, stack):
    print('Alarm: ', time.ctime())


# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print()
print('Before: ', time.ctime())
time.sleep(4)
print('After: ', time.ctime())
