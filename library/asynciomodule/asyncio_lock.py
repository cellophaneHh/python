'''
asyncio.Lock()用于共享资源的同步访问
三个方法
acquire() 请求锁
release() 释放锁
locked() 检测状态
'''
import asyncio
import functools


def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def coro1(lock):
    print('coro1 waiting for the lock')
    async with lock:
        print('coro1 acquired lock')
    print('coro1 released lock')


async def coro2(lock):
    print('coro2 waiting for th lock')
    await lock.acquire()
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()


async def main(loop):
    lock = asyncio.Lock()
    print('acquiring the lock before starting coroutines')
    await lock.acquire()
    print('lock acquired: {}'.format(lock.locked()))

    # 过一段时间之后释放锁
    loop.call_later(1, functools.partial(unlock, lock))

    # 协程中使用锁
    print('waiting for coroutines')
    await asyncio.wait([coro1(lock), coro2(lock)])


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
