'''
选择排序
'''
import numpy as np
import time


class Selection:

    @staticmethod
    def sort(data):
        len_data = len(data)
        for i in range(0, len_data):
            min_index = i
            for j in range(i + 1, len_data):
                if data[j] < data[min_index]:
                    min_index = j
            Selection.exchange(data, i, min_index)

    @staticmethod
    def exchange(data, i, j):
        temp = data[j]
        data[j] = data[i]
        data[i] = temp


# data = np.random.randint(0, 100, 10)
# print(data)
# Selection.sort(data)
# print(data)
