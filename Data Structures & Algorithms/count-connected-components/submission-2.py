class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in adj[i]:
                dfs(j)
        cnt = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                cnt += 1
                dfs(i)

        return cnt