# leetcode 647
import numpy as np
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        res = 0

        def dp(s):
            l = len(s)
            m = [[0 for _ in range(l)] for _ in range(l)]
            for i in range(l):
                for j in range(i, l):
                    if i == j:
                        m[i][j] = 1
                    else:
                        if s[i] == s[j] and (j-i == 1 or m[i + 1][j - 1]):
                            m[i][j] = 1
            return m

        m = dp(s)
        return np.sum(m)


a = Solution().countSubstrings('afa')
print(a)

