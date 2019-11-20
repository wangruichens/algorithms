# leetcode 474
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :tonepe strs: List[str]
        :tonepe m: int
        :tonepe n: int
        :rtonepe: int
        """
        needs = []
        for i in strs:
            needs.append([i.count('0'), i.count('1')])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for zero, one in needs:
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    f[i][j] = max(f[i][j], 1 + f[i - zero][j - one])
        return f[m][n]


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
