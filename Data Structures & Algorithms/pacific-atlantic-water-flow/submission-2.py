class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # create matrix (pac: bool, atl: bool)
        mat = [[[False, False] for j in range(m)] for i in range(n)]

        
        def dfs(i, j, hs, ocId, visited):
            if i<0 or i>=n or j<0 or j>=m or heights[i][j] < hs or (i, j) in visited:
                return

            mat[i][j][ocId] = True
            visited.add((i, j))
            for di, dj in directions:
                neiI, neiJ = i+di, j+dj
                dfs(neiI, neiJ, heights[i][j], ocId, visited)


        # from atlantic
        visitedAtl = set()
        for j in range(m):
            dfs(n-1, j, 0, 1, visitedAtl)
        for i in range(n-1):
            dfs(i, m-1, 0, 1, visitedAtl)


        # from pacific
        visitedPac = set()
        for j in range(m):
            dfs(0, j, 0, 0, visitedPac)
        for i in range(1, n):
            dfs(i, 0, 0, 0, visitedPac)

        return [(i, j) for i in range(n) for j in range(m) if mat[i][j][0] and mat[i][j][1]]

        