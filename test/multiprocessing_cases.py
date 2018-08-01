from multiprocessing import freeze_support, Pool
import time


def Foo(i):
    time.sleep(2)
    return i * 2


def Bar(arg):
    print('done', arg)


if __name__ == '__main__':
    freeze_support()
    pool = Pool(2)

    for i in range(3):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)

    print('end')
    pool.close()
    pool.join()
