# leetcode 84
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        tmp = []
        heights = [0] + heights + [0]
        area = 0
        for i, v in enumerate(heights):
            while tmp and heights[tmp[-1]] > v:
                idx = tmp.pop()
                h = heights[idx]
                area = max(area, (i - tmp[-1] - 1) * h)
            tmp.append(i)

        return area
