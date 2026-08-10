class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = [[False for j in range(n)] for i in range(n)]
        for e in edges:
            a, b = e
            g[a][b] = True
            g[b][a] = True
        def dfs(i, bef):
            if i in visited:
                return False
            visited.add(i)
            for j in range(n):
                if not g[i][j] or j==bef:
                    continue
                if not dfs(j, i):
                    return False
            return True


        visited = set()
        return dfs(0, None) and len(visited)==n

