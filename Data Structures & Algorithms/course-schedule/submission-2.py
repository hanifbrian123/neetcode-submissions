class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            g[a].append(b)

        safeNodes = set()
        def dfs(i, cur):
            if i is None:
                return True
            elif i in safeNodes:
                return True
            elif i in cur:
                return False
            
            cur.add(i)
            for neiI in g[i]:
                if not dfs(neiI, cur):
                    return False
            safeNodes.add(i)
            return True

        for i in range(len(g)):
            if i not in safeNodes:
                cur = set()
                if not dfs(i, cur):
                    return False
        return True
