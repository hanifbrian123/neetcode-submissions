class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[None] * m for i in range(n)]
        def dfs(i, j):
            if i<0 or j<0 or i>=n or j>=m or obstacleGrid[i][j] == 1:
                return 0
            elif i == n-1 and j == m-1:
                return 1
            elif dp[i][j] is not None:
                return dp[i][j]
            
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]

        return dfs(0, 0)
