import asyncio
import time


async def work(semaphore):
    async with semaphore:
        await asyncio.sleep(2)
        print("{}".format(time.time()))


async def main():
    semaphore = asyncio.Semaphore(2)
    tasks = [work(semaphore) for i in range(10)]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
