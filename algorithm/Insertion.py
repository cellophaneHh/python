'''
插入排序
'''


class Insertion:

    @staticmethod
    def sort(data):
        len_data = len(data)
        for i in range(1, len_data):
            for j in range(i, 0, -1):
                if data[j] < data[j - 1]:
                    Insertion.exchange(data, j, j - 1)

    @staticmethod
    def sort_advance(data):
        len_data = len(data)
        for i in range(1, len_data):
            temp = data[i]
            for j in range(i, 0, -1):
                if data[j - 1] > temp:
                    data[j] = data[j - 1]
                else:
                    break
            data[j - 1] = temp

    @staticmethod
    def exchange(data, i, j):
        temp = data[j]
        data[j] = data[i]
        data[i] = temp
