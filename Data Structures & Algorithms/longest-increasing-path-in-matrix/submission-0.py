class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        n, m = len(matrix), len(matrix[0])
        def dfs(i, j, bef):
            if i<0 or j<0 or i>=n or j>=m or bef >= matrix[i][j]:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            num = matrix[i][j]
            dp[(i, j)] = 1 + max(
                dfs(i+1, j, num),
                dfs(i-1, j, num),
                dfs(i, j+1, num),
                dfs(i, j-1, num)
            )
            return dp[(i, j)]

        res = 1
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j, -1))
        return res