
def binary_search(key, key_list):
    low = 0
    high = len(key_list) - 1
    while low <= high:
        mid = round((low + high) / 2)
        if key > key_list[mid]:
            low = mid + 1
        elif key < key_list[mid]:
            high = mid - 1
        else:
            return mid
    return -1


keys = [1, 4, 8, 10, 23, 45, 19]
print(binary_search(10, keys))
print(binary_search(11, keys))
print(binary_search(23, keys))

