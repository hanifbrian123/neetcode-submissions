class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i+1:[] for i in range(len(edges))}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        eInTheCycle = set()
        finishTheCycle = False
        def dfs(i, bef):
            nonlocal finishTheCycle
            if i in visited:
                return i
            visited.add(i)
            for nei in adj[i]:
                if nei==bef:
                    continue
                a = dfs(nei, i)
                if a is not None:
                    if not finishTheCycle:
                        eInTheCycle.add((i, nei))
                    if i == a:
                        finishTheCycle = True
                    return a
        visited = set()
        a = dfs(1, 0)
        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i][0], edges[i][1]
            if (u, v) in eInTheCycle or (v, u) in eInTheCycle:
                return [u, v]

            



