# leetcode 95
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
            for val in range(start, end + 1):
                for left in helper(start, val - 1):
                    for right in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return helper(1, n)
