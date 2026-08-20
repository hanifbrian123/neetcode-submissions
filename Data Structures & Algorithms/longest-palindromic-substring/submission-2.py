class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]
        resIdx = 0
        lenIdx = 1
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1] is True):
                    dp[i][j] = True
                    if j-i+1 > lenIdx:
                        lenIdx = j-i+1
                        resIdx = i
        return s[resIdx:resIdx+lenIdx]