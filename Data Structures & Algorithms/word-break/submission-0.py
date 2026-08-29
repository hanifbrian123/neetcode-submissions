class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[-1] = True
        for i in range(n-1, -1, -1):
            for w in wordDict:
                m = len(w)
                if i+(m-1) < n and s[i:i+m] == w:
                    dp[i] = True
                    break
        return dp[0]