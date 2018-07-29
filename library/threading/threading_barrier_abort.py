'''
abort中断wait，并抛出BrokenBarrierError异常
'''
import threading
import time


def worker(barrier):
    print(threading.current_thread().name,
          'warting for barrier with {} others'.format(
              barrier.n_waiting))
    try:
        # 在这里会阻塞
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        # 中断
        print(threading.current_thread().name, 'aborting')
    else:
        # 正常结束等待时
        print(threading.current_thread().name, 'after barrier', worker_id)


NUM_THREADS = 3

# 多了一个用于不让线程结束等待。。。。
barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
    threading.Thread(
        name='woerk-%s' % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'starting')
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()
