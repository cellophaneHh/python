'''
asyncio.Queue()  先进先出队列

get()方法获得一个元素, 空会阻塞
task_done()， 每次get()之后调用task_done()告知队列此次访问已经完成

join()方法用于等待队列为空, 即所有元素都被get()并且task_done()方法被调用

'''

import asyncio


async def consumer(n, q):
    print('consumer {}: starting'.format(n))
    while True:
        print('consumer {}: waiting for item'.format(n))
        item = await q.get()
        print('consumer {}: has item {}'.format(n, item))
        if item is None:
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print('consumer {}: ending'.format(n))


async def producer(q, num_workers):
    print('producer: starting')
    for i in range(num_workers * 3):
        await q.put(i)
        print('producer: added task {} to the queue'.format(i))

    # 添加None值标识结束
    print('producer : adding stop signals to the queue')
    for i in range(num_workers):
        await q.put(None)
    print('producer: waiting for queue to empty')
    await q.join()
    print('producer: ending')


async def main(loop, num_consumers):
    q = asyncio.Queue(maxsize=num_consumers)
    consumers = [
        loop.create_task(consumer(i, q)) for i in range(num_consumers)
    ]

    prod = loop.create_task(producer(q, num_consumers))

    await asyncio.wait(consumers + [prod])


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop, 2))
