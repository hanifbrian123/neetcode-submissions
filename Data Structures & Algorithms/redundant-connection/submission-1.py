class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i+1:[] for i in range(len(edges))}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        eInTheCycle = set()
        def dfs(i, bef):
            if i in visited:
                return i
            visited.add(i)
            for nei in adj[i]:
                if nei==bef:
                    continue
                a = dfs(nei, i)
                if a is not None:
                    eInTheCycle.add((i, nei))
                    return a
        visited = set()
        a = dfs(1, 0)
        print(f"a: {a}")
        print(eInTheCycle)
        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i][0], edges[i][1]
            if (u, v) in eInTheCycle or (v, u) in eInTheCycle:
                return [u, v]
        # visited = set()
        # a = dfs(1, 0)
        # print(a)
        # visitedRes = set()
        # edgesInCycle = set()
        # def dfsAddRes(i, bef):
        #     if (i, bef) in visitedRes:
        #         return True
        #     if bef != 0:
        #         visitedRes.add((i, bef))
        #     for nei in adj[i]:
        #         if nei == bef:
        #             continue
        #         arrived = dfsAddRes(nei, i)
        #         if arrived:
        #             edgesInCycle.add((i, nei))
        #             return True
        #     return False
        # dfsAddRes(a, 0)
        # print(edgesInCycle)
        # print(visitedRes)

        return [0, 0]
        # for i in range(len(edges)-1, -1, -1):
        #     u, v = edges[i]
        #     if (u, v) in visitedRes or (v, u) in visitedRes:
        #         return [u, v]

            



