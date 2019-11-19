# leetcode 332
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


print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
