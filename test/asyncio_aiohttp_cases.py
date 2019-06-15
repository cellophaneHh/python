import asyncio
import aiohttp
import time


async def task(url, loop, session):
    async with session.get(url, timeout=10) as response:
        status = response.status
        print(status)
        response.encoding = 'utf-8'
        if status == 200:
            content = await response.text()
            print(content)
            return content


urls = []
for i in range(1):
    urls.append('http://baike.baidu.com/item/王世桢')
session = aiohttp.ClientSession()
event_loop = asyncio.get_event_loop()
try:
    todo = [task(url, event_loop, session) for url in urls]
    waits = asyncio.wait(todo)
    now = time.time()
    event_loop.run_until_complete(waits)
    print(time.time() - now)
finally:
    pass
    #event_loop.close()
