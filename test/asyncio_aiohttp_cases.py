import asyncio
import aiohttp
import time


async def task(url, loop):
    async with aiohttp.get(url) as response:
        return await response.status


urls = []
for i in range(10):
    urls.append('http://httpbin.org')
event_loop = asyncio.get_event_loop()
try:
    todo = [task(url, event_loop) for url in urls]
    waits = asyncio.wait(todo)
    now = time.time()
    event_loop.run_until_complete(waits)
    print(time.time() - now)
finally:
    event_loop.close()
