import threading
import logging
import queue
import random
import time


logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)s %(message)s)'
)

task_queue = queue.Queue(maxsize=10)


class Sender(threading.Thread):

    def __init__(self, task_queue):
        threading.Thread.__init__(self)
        self.task_queue = task_queue

    def run(self):
        while True:
            try:
                task_queue.put(random.randint(1, 3))
            except Exception as e:
                logging.error("添加失败, 当前队列大小: {}".format(str(len(self.task_queue))))


class Receiver(threading.Thread):

    def __init__(self, task_queue):
        threading.Thread.__init__(self)
        self.task_queue = task_queue

    def run(self):
        while True:
            task = self.task_queue.get()
            logging.info("sleep time: {}".format(str(task)))
            time.sleep(task)
            task_queue.task_done()


sender = Sender(task_queue)
receiver = Receiver(task_queue)

sender.start()
receiver.start()




