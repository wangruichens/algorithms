# leetcode 332
# 欧拉回路： 删除一个结点后，仍是欧拉回路
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        res = []
        for x, y in sorted(tickets)[::-1]:
            graph[x].append(y)

        def dfs(tmp):
            while graph[tmp]:
                dfs(graph[tmp].pop())
            res.append(tmp)

        dfs("JFK")
        return res[::-1]
