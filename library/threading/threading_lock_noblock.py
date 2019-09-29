'''
acquire(blocking=True, timeout=-1)
'''
import logging
import threading
import time


def lock_holder(lock):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)


def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        have_it = lock.acquire(False)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired', num_tries)
            else:
                logging.debug('Iteration %d: Not acquired', num_tries)
            if num_tries > 10:
                break
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s')

lock = threading.Lock()

# holder = threading.Thread(
#     target=lock_holder,
#     args=(lock,),
#     name='LockHolder',
#     daemon=True,
# )

worker = threading.Thread(
    target=worker,
    args=(lock, ),
    name='Worker',
)
worker.start()
worker.join()
