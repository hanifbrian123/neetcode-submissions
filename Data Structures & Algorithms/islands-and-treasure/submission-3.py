class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(i, j):
            q = collections.deque([(i, j)])
            visited = {(i, j)}
            level = -1
            while q:
                size = len(q)
                level += 1
                for _ in range(size):
                    i, j = q.popleft()
                    for mv in moves:
                        neiI, neiJ = i+mv[0], j+mv[1]
                        if (
                            neiI < 0 or neiI >= n or neiJ < 0 or neiJ >= m or 
                            (neiI, neiJ) in visited or grid[neiI][neiJ] < 0
                        ): continue
                        if grid[neiI][neiJ] == 0:
                            return level+1
                        
                        visited.add((neiI, neiJ))
                        q.append((neiI, neiJ))
            return float('inf')


        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    d = bfs(i, j)
                    grid[i][j] = d