# leetcode 174 地下城游戏
# 逆向动态规划
# 1.最优化原理（最优子结构性质）
# 2.无后向性 (or 无前向性 or 单一方向性)
# 3.子问题的重叠性
# ** 有点类似于01背包问题，内层循环必须也是逆序的
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        if row == 0:
            return 0
        col = len(dungeon[0])
        dp = [0 for _ in range(col)]
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if i == row - 1 and j == col - 1:
                    dp[-1] = max(1, 1 - dungeon[i][j])
                elif i == row - 1:
                    dp[j] = max(1, dp[j + 1] - dungeon[i][j])
                elif j == col - 1:
                    dp[j] = max(1, dp[j] - dungeon[i][j])
                else:
                    dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0]


print(Solution().calculateMinimumHP([[1, -3, 3], [0, -2, 0], [-3, -3, -3]]))
