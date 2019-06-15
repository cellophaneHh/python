'''
Condition和Event类似
但是Event会唤醒所有等待的任务
而Condition则可以通过notify(n)方法中的n参数控制唤醒的任务的数量
                通过notify_all()方法唤醒所有的任务
'''

import asyncio


async def consumer(condition, n):
    async with condition:
        print('consumer {} is waiting'.format(n))
        await condition.wait()
        print('consuemr {} triggered'.format(n))
    print('ending consumer {}'.format(n))


async def manipulate_condition(condition):
    print('starting manupulate_condition')

    # 等待一段时间让consumer启动
    await asyncio.sleep(0.1)

    for i in range(1, 3):
        async with condition:
            print('notifying {} consumers'.format(i))
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    async with condition:
        print('notifying remaining consumers')
        condition.notify_all()

    print('ending manupulate_condition')


async def main(loop):
    condition = asyncio.Condition()

    consumers = [consumer(condition, i) for i in range(5)]

    loop.create_task(manipulate_condition(condition))
    await asyncio.wait(consumers)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
