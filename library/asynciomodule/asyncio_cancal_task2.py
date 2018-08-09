'''
如果被取消的任务中存在另外一个操作，
这个任务会在等待这个的地方抛出CancelledError异常
'''

import asyncio


async def task_func():
    print('in task_func, sleeping')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task_func was canceled')
        raise
    return 'the result'


def task_canceller(t):
    print('in task_canceller')
    t.cancel()
    print('canceled the task')


async def main(loop):
    print('creating task')
    # 创建一个等待另外一个异步任务的任务
    task = loop.create_task(task_func())
    # 对任务调用取消操作
    loop.call_soon(task_canceller, task)

    try:
        # 上面调用了取消操作，这里会抛出错误
        await task
    except asyncio.CancelledError:
        print('main() also sees task as cancelled')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
