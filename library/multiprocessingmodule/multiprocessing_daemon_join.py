import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print('Starting: ', name)
    time.sleep(2)
    print('Exiting: ', name)


def non_daemon():
    name = multiprocessing.current_process().name
    print('Starting: ', name)
    print('Exiting: ', name)


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
        daemon=True,
    )

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
