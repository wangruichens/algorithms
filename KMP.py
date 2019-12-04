# leetcode 28 KMP匹配
class Solution:
    def strStr(self, t, p):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not p: return 0
        _next = [0] * len(p)

        def getNext(p, _next):
            _next[0] = -1
            i = 0
            j = -1
            while i < len(p) - 1:
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]

        getNext(p, _next)
        print(_next)
        i = 0
        j = 0
        while i < len(t) and j < len(p):
            if j == -1 or t[i] == p[j]:
                i += 1
                j += 1
            else:
                j = _next[j]
        if j == len(p):
            return i - j
        return -1


print(Solution().strStr('cabababcac', 'aaaa'))

# leetcode 214 最短回文串
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = s[::-1]
        if s == rs:
            return s

        def kmp(s):
            next = [0] * len(s)
            next[0] = -1
            i = 0
            j = -1
            while i < len(s) - 1:
                if j == -1 or s[i] == s[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]
            return next

        next = kmp(s)
        rs = s[::-1]
        i = 0
        j = 0
        while i < len(rs):
            if j == -1 or rs[i] == s[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        pre = rs[:i - j]
        return pre + s
print(Solution().shortestPalindrome('aacecaaa'))

