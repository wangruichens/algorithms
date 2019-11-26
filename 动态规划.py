# leetcode 312 戳气球
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][-1]


# leetcode 390
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            return 2 * (n / 2 + 1 - self.lastRemaining(n / 2))


# leetcode 97 交错字符串
# 二维DP解法
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        row = len(s1)
        col = len(s2)

        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        dp[0][0] = True

        for i in range(row + 1):
            for j in range(col + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                            dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[row][col]


# leetcode 97 交错字符串
# 一维DP化简
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        row = len(s1)
        col = len(s2)
        if row + col != len(s3):
            return False
        dp = [False for _ in range(row + 1)]
        dp[0] = True
        for j in range(col + 1):
            for i in range(row + 1):
                if j == 0 and i == 0:
                    dp[i] = True
                elif i == 0:
                    dp[i] = dp[i] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i] = dp[i - 1] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i] = (dp[i] and s2[j - 1] == s3[i + j - 1]) or (dp[i - 1] and s1[i - 1] == s3[i + j - 1])
        return dp[-1]
