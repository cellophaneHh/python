"""
future
"""

import asyncio
import time


def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    time.sleep(3)
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print('scheduling mark_done')
    event_loop.call_soon(mark_done, all_done, 'the result')
    print('enter event loop')
    result = event_loop.run_until_complete(all_done)
    print('returned result: {!r}'.format(result))
finally:
    event_loop.close()
    pass
