"""
在某个时间点调用
"""

import asyncio
import time


def callback(n, loop):
    print('callback {} invoked at {}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('clock time: {}'.format(time.time()))
    print('loop time: {}'.format(now))

    print('registering callbacks')
    loop.call_at(now + 2, callback, 1, loop)
    loop.call_at(now + 1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)
    await asyncio.sleep(3)


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    # event_loop.close()
    pass
