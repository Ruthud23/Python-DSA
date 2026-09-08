class Solution:
    def moveZeroes(self, nums):
        result = []
        for num in nums:
            if num != 0:
                result.append(num)

        while len(result) < len(nums):
                result.append(0)

        for i in range(len(nums)):
            nums[i] = result[i]
         
        
        