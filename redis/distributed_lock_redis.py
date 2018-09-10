'''
redis实现的分布式锁
'''
import redis_pool
import redis
import threading
import time


redis_client = redis.Redis(connection_pool=redis_pool.pool)


def task():
    print(threading.current_thread().name)


def doSomething():
    '''
    分布式锁实现，没有时设置并设置超时时间，完成任务后删除
    会有任务超过锁超时时间的问题。。。
    '''
    try:
        redis_client.set('lock', 1, ex=20, nx=True)
        for i in range(3):
            task()
            time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        redis_client.delete('lock')


if __name__ == '__main__':
    threads = []
    for i in range(3):
        t = threading.Thread(
            name='thread-' + str(i),
            target=doSomething,
            daemon=True)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
