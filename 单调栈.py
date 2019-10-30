# leetcode 84
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = []
        heights = [0] + heights + [0]
        area = 0
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:
                idx = stack.pop()
                h = heights[idx]
                area = max(area, (i - stack[-1] - 1) * h)
            stack.append(i)

        return area


# leetcode 739
class Solution(object):
    def dailyTemperatures(self, T):
        stack = []
        res = [0] * len(T)
        for i, v in enumerate(T):
            while stack and T[stack[-1]] < v:
                pos = stack.pop()
                res[pos] = i - pos
            stack.append(i)
        return res
