# leetcode 137
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = 0
        for i in nums:
            two |= (one & i)
            one = one ^ i
            three = (one & two)

            one &= ~three
            two &= ~three
        return one
