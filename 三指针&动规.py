# leetcode 264
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        n2 = n3 = n5 = 0
        res = [1]
        while len(res) < n:
            tmp = min(2 * res[n2], 3 * res[n3], 5 * res[n5])
            res.append(tmp)
            # 当前最小丑数用掉了， 对应指针+1
            if tmp == 2 * res[n2]:
                n2 += 1
            if tmp == 3 * res[n3]:
                n3 += 1
            if tmp == 5 * res[n5]:
                n5 += 1
        return res[-1]


Solution().nthUglyNumber(10)


# leetcode 1262
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, -float('inf'), -float('inf')]
        for i in nums:
            dp2 = dp[::]
            for j in range(3):
                dp2[(i + j) % 3] = max(dp[(i + j) % 3], dp[j] + i)
            dp = dp2
        return dp[0]


print(Solution().maxSumDivThree([3, 6, 5, 1, 8]))
