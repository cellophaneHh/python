import asyncio


async def work():
    print("asdfasdf")
    await asyncio.sleep(1)
    print('12341234')


async def main(loop):
    works = [work() for i in range(5)]
    await asyncio.wait(works)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
