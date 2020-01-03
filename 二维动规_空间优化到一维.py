#leetcode 516 最长回文子序列
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        dp = [[0] * l for _ in range(l)]
        for dis in range(l):
            for x in range(l - dis):
                y = x + dis
                if x == y:
                    dp[x][y] = 1
                else:
                    if s[x] == s[y]:
                        dp[x][y] = dp[x + 1][y - 1] + 2
                    else:
                        dp[x][y] = max(dp[x][y-1], dp[x+1][y])
        return dp[0][-1]

    def longestPalindromeSubseq(self, s):
        l = len(s)
        cur = [0] * l

        for j in range(l - 1, -1, -1):
            pre = cur[:]
            for i in range(j, l):
                if i == j:
                    cur[i] = 1
                else:
                    if s[i] == s[j]:
                        cur[i] = pre[i - 1] + 2
                    else:
                        cur[i] = max(cur[i - 1], pre[i])
        return cur[-1]


print(Solution().longestPalindromeSubseq('bbbab'))
