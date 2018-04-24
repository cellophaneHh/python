from generators import int_generator_random


def selSort(L):
    """假设L是列表，其中元素可以用>进行比较，对L进行升序排序"""
    suffixStart = 0
    while suffixStart != len(L):
        # 检查后缀集合中的每个元素
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                # 交换元素位置
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1


L = list(int_generator_random(100))
print(L)
selSort(L)
print(L)
