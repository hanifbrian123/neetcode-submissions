class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1 for i in range(n)]
        dToL = {str(i-64):chr(i) for i in range(65,65+26)}
        def dfs(sIdx, take):
            if sIdx+take>=n:
                return 0
            
            d = s[sIdx+1] if take==1 else s[sIdx+1]+s[sIdx+2]
            if d not in dToL:
                return 0
            
            if dp[sIdx+take] != -1:
                return dp[sIdx+take]
            
            tot = max(1, dfs(sIdx+take, 1) + dfs(sIdx+take, 2))
            dp[sIdx+take] = tot
            return tot
        return dfs(-1, 1) + dfs(-1, 2)