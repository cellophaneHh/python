import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.options('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text(encoding='utf-8'))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
