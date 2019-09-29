"""
最大子序和
"""


class Solution:
    def maxSubArray(self, nums):
        ans = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            if sum > ans:
                ans = sum
        return ans


solution = Solution()
print(solution.maxSubArray([1, 2, 3, -1, 10, 1]))
