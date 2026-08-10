class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(i, bef):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if j==bef:
                    continue
                if not dfs(j, i):
                    return False
            return True


        visited = set()
        return dfs(0, -1) and len(visited)==n

