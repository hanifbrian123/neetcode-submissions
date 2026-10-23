class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[None] * m for i in range(n)]
        dp[n-1][m-1] = grid[n-1][m-1]
        def dfs(i, j):
            if i<0 or j<0 or i>=n or j>=m:
                return float('inf')
            elif dp[i][j] is not None:
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
            return dp[i][j]

        return dfs(0, 0)
