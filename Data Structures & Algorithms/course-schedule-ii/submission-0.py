class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            g[a].append(b)

        safeNodes = set()
        res = []
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
            res.append(i)
            return True

        for i in range(len(g)):
            if i not in safeNodes:
                cur = set()
                if not dfs(i, cur):
                    return []
        return res