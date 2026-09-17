class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        best = INF
        ans = INF

        # min_len[i] = shortest subarray with sum target
        # ending before index i
        min_len = [INF] * (n + 1)

        left = 0
        curr = 0

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                # Previous subarray must end before left
                if min_len[left] != INF:
                    ans = min(ans, length + min_len[left])

                best = min(best, length)

            min_len[right + 1] = best

        return -1 if ans == INF else ans