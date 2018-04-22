def sumDigits(strs):
    """s为数字组成的字符串，切分后求和"""
    result = 0
    for s in strs:
        try:
            curI = int(s)
            result += curI
        except ValueError:
            pass
    return result

r = sumDigits("a1dfdddd333333")
print(str(r))


def findAnEvent(L):
    """L 为整数列表，返回其中e的i 第一个偶数，如果没有则抛出异常"""
    firstEvent = -1
    for i in L:
        if i % 2 == 0:
            firstEvent = i
            break

    if firstEvent == -1:
        raise ValueError("not found")

findAnEvent([1,3])
