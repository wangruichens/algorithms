# leetcode 229
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) // 3
        res = [0, 0]
        c = [0, 0]
        for i in nums:
            if i not in res:
                if 0 in c:
                    pos = c.index(0)
                    res[pos] = i
                    c[pos] += 1
                else:
                    c[0] -= 1
                    c[1] -= 1
            else:
                pos = res.index(i)
                c[pos] += 1
        return [r for r in set(res) if nums.count(r) > n]
