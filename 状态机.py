# leetcode 309
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold=0
        rest=0
        #第一天只能买入
        hold = float('-inf')
        for p in prices:
            presold= sold
            sold = hold+p
            hold = max(hold , rest-p)
            rest= max(rest,presold)
        return max(sold,rest)

