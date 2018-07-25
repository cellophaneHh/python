'''
可以由任意线程发送alarm信号，但是信号必须是主线程接收
'''
import signal
import time
import threading


def signal_handler(num, stack):
    print(time.ctime(), 'Alarm in',
          threading.currentThread().name)


# 主线程接受alarm信号
signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    t_name = threading.currentThread().name
    print(time.ctime(), 'Setting alarm in', t_name)
    # 可以在任意线程中发送alarm信号
    signal.alarm(1)
    print(time.ctime(), 'Sleeping in', t_name)
    time.sleep(3)
    print(time.ctime(), 'Done with sleep in', t_name)


alarm_thread = threading.Thread(
    target=use_alarm,
    name='alarm_thread',
)
alarm_thread.start()
time.sleep(0.1)

print(time.ctime(), 'Waiting for', alarm_thread.name)
alarm_thread.join()
print(time.ctime(), 'Exiting normally')
