import signal
import time
import threading

def my_handler(num, stack):
    print('signal: ', num)


def receiver():
    try:
        signal.signal(signal.SIGALRM, my_handler)
    except ValueError as ve:
        print('failed to get signal')


def sender():
    signal.alarm(4)



receiver()
#rece = threading.Thread(
#    target=receiver,
#    name='receiver')
send = threading.Thread(
    target=sender,
    name='send')
#rece.start()
send.start()

#rece.join()
send.join()
print('Done..')
