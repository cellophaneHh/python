import asyncio


async def main(loop):
    loop.call_soon(lambda x: print(x), 100)

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
