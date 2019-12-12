# leetcode 130
class Solution:
	def solve(self, board):
		"""
		Do not return anything, modify board in-place instead.
		"""
		f = {}

		def find(x):
			f.setdefault(x, x)
			if f[x] != x:
				f[x] = find(f[x])
			return f[x]

		def union(x, y):
			f[find(y)] = find(x)

		if not board or not board[0]:
			return
		row = len(board)
		col = len(board[0])
		dummy = row * col
		for i in range(row):
			for j in range(col):
				if board[i][j] == "O":
					if i == 0 or i == row - 1 or j == 0 or j == col - 1:
						union(i * col + j, dummy)
					else:
						for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
							if board[i + x][j + y] == "O":
								union(i * col + j, (i + x) * col + (j + y))
		for i in range(row):
			for j in range(col):
				if find(dummy) == find(i * col + j):
					board[i][j] = "O"
				else:
					board[i][j] = "X"

# leetcode 547 朋友圈
class Solution(object):
	def findCircleNum(self, M):
		"""
        :type M: List[List[int]]
        :rtype: int
        """
		if len(M) == 0:
			return 0
		row = len(M)
		col = len(M[0])
		p = [-1] * col

		def find(parents, i):
			if parents[i] == -1:
				return i
			return find(parents, parents[i])

		def union(parents, x, y):
			xp = find(parents, x)
			yp = find(parents, y)
			if xp != yp:
				parents[xp] = yp

		for j in range(row):
			for i in range(col):
				if M[i][j] == 1:
					union(p, i, j)
		return p.count(-1)


Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
