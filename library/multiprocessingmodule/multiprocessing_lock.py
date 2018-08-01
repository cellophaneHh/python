import multiprocessing
import sys


def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n')


def woker_no_with(lock, stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()


lock = multiprocessing.Lock()
w = multiprocessing.Process(
    target=worker_with,
    args=(lock, sys.stdout),
)
nw = multiprocessing.Process(
    target=woker_no_with,
    args=(lock, sys.stdout),
)

nw.start()
w.start()

w.join()
nw.join()
