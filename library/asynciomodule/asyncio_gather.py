'''
通过gather仅收集返回的结果
'''
import asyncio


async def phase1():
    print('in phase1')
    await asyncio.sleep(2)
    print('done with phase1')
    return 'phase1 result'


async def phase2():
    print('in phase2')
    await asyncio.sleep(1)
    print('done with phase2')
    return 'phase2 result'


async def main():
    print('starting main')
    print('waiting for phases to complete')
    # 仅收集返回的结果
    results = await asyncio.gather(phase1(), phase2())
    print('result: {!r}'.format(results))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
