class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = [[False for j in range(n)] for i in range(n)]
        for e in edges:
            a, b = e
            g[a][b] = True
            g[b][a] = True
        def dfs(i, cur, bef):
            if i in cur:
                return False
            cur.add(i)
            for j in range(n):
                if not g[i][j] or j==bef:
                    continue
                if not dfs(j, cur, i):
                    return False
            return True


        visited = set()
        for i in range(n):
            if i not in visited:
                cur = set()
                if not dfs(i, cur, None):
                    print(cur, visited)
                    return False
                for c in cur:
                    visited.add(c)
        return True
            

