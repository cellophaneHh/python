"""
延迟调用
"""

import asyncio


def callback(n):
    print('callback {} invoked'.format(n))


async def main(loop):
    print('registering callbacks')
    loop.call_later(2, callback, 1)
    loop.call_later(1, callback, 2)
    loop.call_soon(callback, 3)

    await asyncio.sleep(3)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    pass
