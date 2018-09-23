'''
排序算法比较
'''
import time
from Insertion import Insertion
from Selection import Selection
from Shell import Shell
from Merge import Merge
import numpy as np
import sys


class SortCompare:

    @staticmethod
    def __sort(algs, data):
        if 'insertion' == algs:
            Insertion.sort(data)
        if 'insertion_advance' == algs:
            Insertion.sort_advance(data)
        if 'selection' == algs:
            Selection.sort(data)
        if 'shell' == algs:
            Shell.sort(data)
        if 'merge' == algs:
            Merge.sort(data)

    @staticmethod
    def compare(algs, data_size):
        data = np.random.randint(0, 1000, data_size)
        start = time.time()
        SortCompare.__sort(algs, data)
        end = time.time() - start
        print('{:<20} {:<10} {:<20}'
              .format(algs, str(data_size), str(end * 1000)))


if __name__ == '__main__':
    data_size = 1000
    if len(sys.argv) > 1:
        data_size = int(sys.argv[1])
    print('{:<20} {:<10} {:<20}'.format('algorithm', 'data_size', 'time(ms)'))
    SortCompare.compare('insertion', data_size)
    SortCompare.compare('insertion_advance', data_size)
    SortCompare.compare('selection', data_size)
    SortCompare.compare('shell', data_size)
    SortCompare.compare('merge', data_size)
