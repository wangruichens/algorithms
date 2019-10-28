# leetcode 416
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        total = total // 2
        t = [True] + [False for _ in range(total)]
        for i in nums:
            for j in range(total, -1, -1):
                if j >= i:
                    t[j] = t[j - i] or t[j]
        return t[total]
