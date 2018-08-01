import multiprocessing
import time


def slow_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')


if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print('before: ', p, p.is_alive())

    p.start()
    print('during: ', p, p.is_alive())

    p.terminate()
    print('terminated: ', p, p.is_alive())
    time.sleep(0.1)
    p.join()  # 这条语句为了给进程状态切换的时间，time.sleep()也可以
    print('joined: ', p, p.is_alive())
