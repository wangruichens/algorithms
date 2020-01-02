# leetcode 300 LIS 最长递增子序列
# 常规动态规划，O(n2)
# class Solution:
#     def lengthOfLIS(self, nums):
#         dp = [1] * len(nums)
#         for i, v in enumerate(nums):
#             for j in range(i):
#                 if nums[j] < v:
#                     dp[i] = max(dp[j] + 1, dp[i])
#         return max(dp)


# 动规+二分查找 O(n*log n)
class Solution:
    def lengthOfLIS(self, nums):
        dp = []

        def binary_search(arr, x):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left

        for i, v in enumerate(nums):
            loc = binary_search(dp, v)
            if loc == len(dp):
                dp.append(v)
            dp[loc] = v
        return len(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


# leetcode 354 套娃信封
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        import bisect
        arr = []
        for _, y in envelopes:
            loc = bisect.bisect_left(arr, y)
            arr[loc:loc + 1] = [y]
        return len(arr)
