import threading
import typing
import time


def worker(semphore) -> (typing.Callable):
    with semphore:
        print('=, {}'.format(threading.current_thread().name))
        time.sleep(1)


print()
threads = []
semphore = threading.Semaphore(3)
for i in range(10):
    t = threading.Thread(name=str(i), target=worker, args=(semphore, ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
