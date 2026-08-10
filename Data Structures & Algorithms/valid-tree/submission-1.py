class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = [[False for j in range(n)] for i in range(n)]
        for e in edges:
            a, b = e
            g[a][b] = True
            g[b][a] = True
        def dfs(i, visited, bef):
            if i in visited:
                return False
            visited.add(i)
            for j in range(n):
                if not g[i][j] or j==bef:
                    continue
                if not dfs(j, visited, i):
                    return False
            return True


        visited = set()
        for i in range(n):
            if i not in visited:
                if not dfs(i, visited, None):
                    return False
        return True
            

