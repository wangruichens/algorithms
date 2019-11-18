# leetcode 331

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        stack = []
        for i in preorder:
            while stack and i == '#' and stack[-1] == '#':
                stack.pop()
                if not stack: return False
                stack.pop()
            stack.append(i)
        return stack == ['#']


Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
