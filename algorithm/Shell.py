'''
希尔排序
'''


class Shell:

    @staticmethod
    def sort(data):
        len_data = len(data)
        h_key = 1
        h_key_line = [h_key]
        while h_key < (len_data // 3):
            h_key = h_key * 3 + 1
            h_key_line.insert(0, h_key)
        for h in h_key_line:
            for i in range(h, len_data):
                step = 0 - h
                for j in range(i, h - 1, step):
                    if data[j] > data[j - h]:
                        break
                    Shell.exchange(data, j, j - h)

    @staticmethod
    def exchange(data, i, j):
        temp = data[i]
        data[i] = data[j]
        data[j] = temp


# import numpy as np
# data = np.random.randint(0, 1000, 2)
# print(data)
# Shell.sort(data)
# print(data)
