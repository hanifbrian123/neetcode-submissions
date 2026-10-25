class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        dp = {}
        def dfs(i, j):
            if j>=lt:
                return 1
            elif i>=ls:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]


            res = dfs(i+1, j)
            if t[j] == s[i]:
                res += dfs(i+1, j+1)
            dp[(i, j)] = res
            return dp[(i, j)]
            
        return dfs(0, 0)