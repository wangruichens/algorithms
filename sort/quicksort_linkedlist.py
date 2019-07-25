class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        s = head
        f = head.next
        while f and f.next:
            f = f.next.next
            s = s.next
        mid = s.next
        s.next = None
        left, right = self.sortList(head), self.sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next
