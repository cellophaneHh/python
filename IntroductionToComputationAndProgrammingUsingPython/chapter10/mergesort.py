from generators import int_generator_random

def merge(left, right, compare):
    """
    假设left和right是两个有序列表，compare定义了一种元素排序规则，
    返回一个新的有序列表(按照compare定义的顺序)，其中包含于(left+right)相同的元素
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
    return result

def mergeSort(L, compare = lambda x, y: x < y):
    """
    假设L是列表，compare定义了L中元素的排序规则，返回一个新的具有L中相同元素的有序列表
    """
    if len(L) < 2:
        return L[:]
    else :
        middle = len(L) // 2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)


L = list(int_generator_random(100))
print(L)
mergeSort(L)
print(L)
