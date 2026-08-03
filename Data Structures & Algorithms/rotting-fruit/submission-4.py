class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numFresh = 0
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: numFresh +=1 
                elif grid[i][j] == 2:
                    q.append((i, j))
                    
        minElapse = 0
        while q:
            size = len(q)
            isRemainAFresh = False
            for _ in range(size):
                i, j = q.popleft()
                for drI, drJ in directions:
                    neiI, neiJ = i+drI, j+drJ
                    if (
                        neiI>=0 and neiI<n and neiJ>=0 and neiJ<m and
                        grid[neiI][neiJ] == 1
                    ):
                        numFresh -= 1
                        q.append((neiI, neiJ))
                        grid[neiI][neiJ] = 2
                        isRemainAFresh = True
            if isRemainAFresh: minElapse += 1

        return minElapse if numFresh == 0 else -1


                

        
        
            