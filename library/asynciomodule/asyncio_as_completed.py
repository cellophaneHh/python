'''
as_completed()方法
对多个任务，不会按顺序返回每个任务，而是先完成的任务先返回
并且不需要等待所有任务都完成,任务完成后就返回了
'''
import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.5 - (0.1 * i))
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [phase(i) for i in range(num_phases)]
    print('waitingh for phases to complete')
    results = []
    # results = await asyncio.gather(*phases)
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('received answer {!r}'.format(answer))
        results.append(answer)
    print('results: {!r}'.format(results))
    return results


loop = asyncio.get_event_loop()
loop.run_until_complete(main(3))
