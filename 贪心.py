# leetcode 45
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxp = 0
        step = 0
        end = 0
        for i in range(len(nums) - 1):
            maxp = max(maxp, nums[i] + i)
            if i == end:
                end = maxp
                step += 1

        return step
