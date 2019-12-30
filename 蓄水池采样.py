# leetcode 382
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import numpy as np


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = 0
        selected = self.head.val
        tmp = self.head.next
        while tmp:
            replace = np.random.randint(0, i + 2)
            if replace == 0:
                selected = tmp.val
            tmp = tmp.next
            i += 1
        return selected
