class Solution:
    def merge(self, nums1, m, nums2, n):
        result = []

        for num in nums1[:m]:
            result.append(num)

        for num in nums2:
            result.append(num)

        result.sort()

        for i in range(len(result)):
            nums1[i] = result[i]