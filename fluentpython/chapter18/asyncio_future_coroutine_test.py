import asyncio


def run_sync(coro_or_future):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coro_or_future)


@asyncio.coroutine
def some_coroutine():
    yield from asyncio.sleep(3)
    return 10

def some_future():
    '''测试future'''
    pass

print(run_sync(some_coroutine()))
