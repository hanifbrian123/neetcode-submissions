class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i, bef):
            if i in visited:
                return i
            visited.add(i)
            for nei in adj[i]:
                if nei==bef:
                    continue
                a = dfs(nei, bef)
                if a is not None:
                    return a
        visited = set()
        a = dfs(1, 0)

        visitedRes = set()
        def dfsAddRes(i, bef):
            if (i, bef) in visitedRes:
                return True
            if bef != 0:
                visitedRes.add((i, bef))
            for nei in adj[i]:
                if nei == bef:
                    continue
                arrived = dfsAddRes(nei, i)
                if arrived:
                    return True
            return False
        dfsAddRes(a, 0)

        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i]
            if (u, v) in visitedRes or (v, u) in visitedRes:
                return [u, v]

            



