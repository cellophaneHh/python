import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    time.sleep(40)
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon1',
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon1',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(30)
    n.start()
