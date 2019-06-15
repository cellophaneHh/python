'''
wait增加timeout超时设置
'''
import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    try:
        await asyncio.sleep(0.1 * i)
    except asyncio.CancelledError:
        print('phase {} canceled'.format(i))
        raise
    else:
        print('done with phase {}'.format(i))
        return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [phase(i) for i in range(num_phases)]
    print('waiting 0.1 for phases to complete')

    complated, pending = await asyncio.wait(phases, timeout=0.1)
    print('{} completed and {} pending'.format(len(complated), len(pending)))

    if pending:
        print('canceling tasks')
        for t in pending:
            t.cancel()
    print('exiting main')


loop = asyncio.get_event_loop()
loop.run_until_complete(main(3))
