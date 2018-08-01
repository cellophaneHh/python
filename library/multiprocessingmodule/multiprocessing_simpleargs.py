'''
给进程的参数必须是可以使用pickle序列化的
'''

import multiprocessing


def worker(num):
    '''thread worker function'''
    print('Worker:', num)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
