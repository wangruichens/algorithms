# leetcode 1044 最长重复子串 （内存超限 MLE）
class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        import numpy as np
        def buildsa(s):
            if not s:
                return []
            ########### 这里可以优化 [2倍增算法] #######################
            suffix = []
            h = [0] * len(s)
            for i in range(len(s)):
                suffix.append(s[i:])
            sa = np.argsort(suffix)
            rk = np.argsort(sa)
            # print(rk)
            # print(sa)
            ##################################
            k = 0
            for i in range(len(s)):
                if rk[i] != 0:
                    if k:
                        k -= 1
                j = sa[rk[i] - 1]
                while j + k < len(s) and i + k < len(s) and s[i + k] == s[j + k]:
                    k += 1
                h[rk[i]] = k
            # print(h)
            maxh = max(h)
            rkidx = h.index(maxh)
            return s[sa[rkidx]:sa[rkidx] + maxh]

        return buildsa(S)


print(Solution().longestDupSubstring('banana'))
