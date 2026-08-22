class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1 for i in range(n)]
        dToL = {str(i-64):chr(i) for i in range(65,65+26)}
        def dfs(sIdx, take):
            if sIdx+take == n-1:
                dp[sIdx+take] = 1
                d = s[sIdx+1] if take==1 else s[sIdx+1]+s[sIdx+2]
                return 1 if d in dToL else 0
            elif sIdx+take >= n:
                return 0
            
            d = s[sIdx+1] if take==1 else s[sIdx+1]+s[sIdx+2]
            if dp[sIdx+take] == -1:
                left = dfs(sIdx+take, 1)
                right = dfs(sIdx+take, 2)
                dp[sIdx+take] = left+right
            
            if d not in dToL:
                return 0
            else:
                return dp[sIdx+take]
        l = dfs(-1, 1)
        r = dfs(-1, 2)
        return l+r
        return dfs(-1, 1) + dfs(-1, 2)