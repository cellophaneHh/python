import multiprocessing as mp


def foo(q):
    q.put('hello')


def set_start_method_use():
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()


def get_context_use():
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()


if __name__ == '__main__':
    set_start_method_use()
    get_context_use()
