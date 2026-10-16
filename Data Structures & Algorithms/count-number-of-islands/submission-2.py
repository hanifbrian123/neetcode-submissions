class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if (
                (i, j) in visited 
                or i < 0 or i >= n or j < 0 or j >= m 
                or grid[i][j] == '0'
            ) :
                return
            visited.add((i, j))
            for d in directions:
                iAdj, jAdj = i+d[0], j+d[1]
                dfs(iAdj, jAdj)

        res = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res