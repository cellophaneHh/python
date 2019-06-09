import asyncio


def save_file(absolute_path, content, encoding='utf-8'):
    print("{}, {}".format(absolute_path, content))
    with open(absolute_path, mode="w", encoding=encoding) as file:
        file.write(content)


async def save_file_coroutine(loop, absolute_path, content, encoding):
    loop.call_soon(save_file, absolute_path, content, encoding)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(
        save_file_coroutine(loop, './123.json', '{}', 'utf-8'))
except Exception:
    raise
finally:
    pass
