class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        falseCache = set() # (i, j)
        def dfs(i, j):
            if i==n and j==m:
                return True
            lookup = j+1 < m and p[j+1] == '*'
            if (i>=n or j>=m):
                return False or (lookup and j+2 >= m)
            if (i, j) in falseCache:
                return False

            if lookup:
                if p[j] == '.' or s[i] == p[j]:
                    if dfs(i, j+2) or dfs(i+1, j+2) or dfs(i+1, j):
                        return True
                else:
                    if dfs(i, j+2):
                        return True
            elif p[j] == '.' or s[i] == p[j]:
                if dfs(i+1, j+1):
                    return True
            
            falseCache.add((i, j))
            return False
        return dfs(0, 0)
"""
a n n _
n * _


a a
. b
"""