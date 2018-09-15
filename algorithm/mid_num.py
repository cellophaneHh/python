'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 不同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5

写的是线性的。。。
log(m + n)的如何实现还需要学习。。
'''
import random


def parttion(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low += 1
        v[high] = v[low]
        v[low] = key
    return low


def quicksort(v, left, right):
    if left < right:
        p = parttion(v, left, right)
        quicksort(v, left, p-1)
        quicksort(v, p+1, right)
    return v


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge_arr = []
        num1_index = 0;
        num1_len = len(nums1)
        num2_index = 0;
        num2_len = len(nums2)
        while num1_index < num1_len and num2_index < num2_len:
            if nums1[num1_index] < nums2[num2_index]:
                merge_arr.append(nums1[num1_index])
                num1_index += 1
            else:
                merge_arr.append(nums2[num2_index])
                num2_index += 1

        while num1_index < num1_len:
            merge_arr.append(nums1[num1_index])
            num1_index += 1
        while num2_index < num2_len:
            merge_arr.append(nums2[num2_index])
            num2_index += 1
        print(merge_arr)
        merge_arr_len = len(merge_arr)
        if merge_arr_len % 2 == 0:
            mid_right = merge_arr_len // 2
            mid_left = mid_right - 1
            return (merge_arr[mid_left] + merge_arr[mid_right]) / 2
        else:
            mid_index = merge_arr_len // 2
            return merge_arr[mid_index]


num1 = [1, 3]
num2 = [3]
# for i in range(random.randint(10, 30)):
#     num1.append(random.randint(1, 10000))
#     num2.append(random.randint(1, 10000))
num1 = quicksort(num1, 0, len(num1) - 1)
num2 = quicksort(num2, 0, len(num2) - 1)

solution = Solution()
print(solution.findMedianSortedArrays(num1, num2))
