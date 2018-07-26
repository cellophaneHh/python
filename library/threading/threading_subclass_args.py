import threading
import logging


class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s',
                      self.args, self.kwargs)


def worker():
    logging.debug('worker...')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s')

for i in range(5):
    t = MyThreadWithArgs(target=worker, args=(i, ),
                         kwargs={'a': 'A', 'b': 'B'})
    t.start()
