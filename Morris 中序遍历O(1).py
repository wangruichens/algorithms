# leetcode 99 恢复二叉搜索树
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        self.tmp = None
        self.w1 = self.w2 = None

        def morris(root):
            cur = root
            while cur:
                if cur.left:
                    pre = cur.left
                    while pre.right and pre.right != cur:
                        pre = pre.right
                    # find the right most node
                    if not pre.right:
                        pre.right = cur
                        cur = cur.left
                        continue
                    else:
                        pre.right = None
                # print(cur.val)
                if self.tmp and cur.val < self.tmp.val:
                    if not self.w1:
                        self.w1 = self.tmp
                    self.w2 = cur

                self.tmp = cur
                cur = cur.right

        morris(root)
        self.w1.val ^= self.w2.val
        self.w2.val ^= self.w1.val
        self.w1.val ^= self.w2.val


a = TreeNode(3)
a.left = TreeNode(1)
a.right = TreeNode(4)
a.right.left = TreeNode(2)
print(Solution().recoverTree(a))
