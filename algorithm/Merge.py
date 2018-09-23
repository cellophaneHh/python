'''
归并排序
'''


class Merge:

    @staticmethod
    def sort(data, left=0, right=-1):
        if len(data) <= 0:
            return
        if right == -1:
            right = len(data) - 1
        Merge.sort_range(data, left, right)

    @staticmethod
    def sort_range(data, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        Merge.sort_range(data, left, mid)
        Merge.sort_range(data, mid + 1, right)
        Merge.merge(data, left, mid, right)

    @staticmethod
    def merge(data, left, mid, right):
        temp = []
        left_start = left
        left_end = mid
        right_start = mid + 1
        right_end = right
        while left_start <= left_end and right_start <= right_end:
            if data[left_start] < data[right_start]:
                temp.append(data[left_start])
                left_start += 1
            else:
                temp.append(data[right_start])
                right_start += 1
        while left_start <= left_end:
            temp.append(data[left_start])
            left_start += 1
        while right_start <= right_end:
            temp.append(data[right_start])
            right_start += 1
        for i in range(len(temp)):
            data[left + i] = temp[i]

    @staticmethod
    def exchange(data, i, j):
        temp = data[i]
        data[i] = data[j]
        data[j] = temp


# import numpy as np
# data = np.random.randint(0, 1000, 6)
# print(data)
# Merge.sort(data, 1, 2)
# print(data)
# Merge.sort(data)
# print(data)
