'''
Event基于threading

用于多个任务需要等待某件事发生
'''

import asyncio
import functools


def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event):
    print('coro1 waiting for event')
    await event.wait()
    print('coro1 triggered')


async def coro2(event):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 triggered')


async def main(loop):
    event = asyncio.Event()
    print('event start state: {}'.format(event.is_set()))

    loop.call_later(1, functools.partial(set_event, event))

    await asyncio.wait([coro1(event), coro2(event)])
    print('event end state: {}'.format(event.is_set()))


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
