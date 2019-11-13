# leetcode 394
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def dfs(s, i):
            res = ""
            multi = 0
            while i < len(s):
                if s[i].isdigit():
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)

    def decodeString2(self, s):
        stack = []
        res = ''
        multi = i = 0
        while i < len(s):
            if s[i].isdigit():
                multi = multi * 10 + int(s[i])
            elif s[i].isalpha():
                res += s[i]
            elif s[i] == '[':
                stack.append([multi, res])
                multi = 0
                res = ''
            elif s[i] == ']':
                m, pre = stack.pop()
                res = pre + res * m
            i += 1
        return res


print(Solution().decodeString2('3[a2[b]]'))
