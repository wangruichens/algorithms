# leetcode 212 单词搜索
# 基本性质
# 1，根节点不包含字符，除根节点以外每个节点只包含一个字符。
# 2，从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串。
# 3，每个节点的所有子节点包含的字符串不相同。
class Solution:
    def findWords(self, board, words):
        # build trie begin ###
        trie = {}
        for word in words:
            t = trie
            for w in word:
                # 有key=w 就返回其value or 添加key = w , value ={}
                t = t.setdefault(w, {})
            t["end"] = 1
        print(trie)
        # build trie end ###
        res = []
        row = len(board)
        col = len(board[0])

        def dfs(i, j, trie, s):
            # print(i, j, trie, s)
            c = board[i][j]
            if c not in trie: return
            trie = trie[c]
            if "end" in trie and trie["end"] != 0:
                res.append(s + c)
                trie["end"] -= 1
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != "#":
                    dfs(tmp_i, tmp_j, trie, s + c)
            board[i][j] = c

        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res


print(Solution().findWords([
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", 'aa', 'oatt', "pea", "eat", "rain"]))
