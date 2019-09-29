import asyncio


async def show():
    await asyncio.sleep(1)
    print(1)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(show())
    x = {'name': [1, 2, 3, 4]}
except Exception:
    pass
