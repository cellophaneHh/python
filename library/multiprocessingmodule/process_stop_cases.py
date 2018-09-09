'''
测试Process如何停止
'''
import multiprocessing
import time


def foo():
    '''永远不会退出的作业'''
    while True:
        print(multiprocessing.current_process().name)
        time.sleep(3)


if __name__ == '__main__':
    cpu_count = multiprocessing.cpu_count()
    p_list = []
    for i in range(cpu_count):
        p = multiprocessing.Process(target=foo, name=str(i))
        p_list.append(p)
    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()
