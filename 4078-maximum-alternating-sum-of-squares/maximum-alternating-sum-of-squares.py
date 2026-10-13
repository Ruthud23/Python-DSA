class Solution:
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        total = 0

        for i in range(n):
            if i < n // 2:
                total -= nums[i] * nums[i]
            else:
                total += nums[i] * nums[i]

        return total