class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i>=n or i<0 or j>=m or j<0 or grid[i][j] != '1' or (i, j) in visited: 
                return
            visited.add((i, j))
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)
        res = 0
        for i in range(n):
            for j in range(m):
                lenA = len(visited)
                dfs(i, j)
                lenB = len(visited)
                if lenB>lenA:
                    res+=1
        return res
