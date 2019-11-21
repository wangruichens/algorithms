# leetcode 491
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, start, tmp):
            # 使用dict去重，常规append + pop TLE。
            dic = {}
            if len(tmp) > 1:
                res.append(tmp[::])
            for i in range(start, len(nums)):
                if dic.get(nums[i], 0):
                    continue
                if not tmp or nums[i] >= tmp[-1]:
                    dic[nums[i]] = 1
                    dfs(nums, i + 1, tmp + [nums[i]])

        dfs(nums, 0, [])
        return res


print(Solution().findSubsequences([4, 6, 7, 7]))
