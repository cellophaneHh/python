"""
二分查找
"""
from generators import int_generator_asc

def search(L, e):
    """假设L是列表，其中元素按升序排列 如果e是L中的元素，则返回True，否则返回False"""

    def bSearch(L, e, low, high):
        if high < low:
            return False
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            return bSearch(L, e, low , mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)

L = list(int_generator_asc(100, 4))
print(L)
print(search(L, 34))


