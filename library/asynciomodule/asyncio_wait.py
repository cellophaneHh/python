import asyncio


async def phase(i):
    print("in phase {}".format(i))
    await asyncio.sleep(0.1 * i)
    print("done with phase {}".format(i))
    return "phase {} result".format(i)


async def main(num_phases):
    print("starting main")
    # 多个任务
    phases = [phase(i) for i in range(num_phases)]
    print("waiting for phase to complete")
    # 并发执行
    completed, pending = await asyncio.wait(phases)
    # 取每个任务的返回值
    results = [t.result() for t in completed]
    print("results: {!r}".format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    pass
