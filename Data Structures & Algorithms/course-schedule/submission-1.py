class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [None for i in range(numCourses)]
        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            g[a] = b
        
        def dfs(i):
            if g[i] in visited:
                res[0] = False
                return
            elif g[i] is None:
                return
            visited.add(i)
            dfs(g[i])
        # print(g)
        for i in range(len(g)):
            visited = set()
            res = [True]
            dfs(i)
            # print(visited)
            if not res[0]:
                return False
        return True

