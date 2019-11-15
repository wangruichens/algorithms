# leetcode 307

class NumArray(object):
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            print(i << 1, i << 1 | 1)
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

        print(self.tree)

    def update(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1

    def sumRange(self, i, j):
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res


a = NumArray([1, 2, 3, 4, 5, 6])
a.sumRange(0, 5)
