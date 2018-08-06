'''
这里有个坑啊
如果在emacs里还是用同一个*Python*缓冲区, 在别的文件里调用过get_event_loop(), 完成后关闭。然后重新调用会报错RuntimeError: Event loop is closed
讲*Python*缓冲取关闭重新打开一个就可以了。。。
'''
import asyncio


async def coroutine():
    print('in coroutine')
    return 'result'


event_loop = asyncio.get_event_loop()
try:
    coro = coroutine()
    return_value = event_loop.run_until_complete(coro)
    print('it returned: {!r}'.format(return_value))
finally:
    event_loop.close()
