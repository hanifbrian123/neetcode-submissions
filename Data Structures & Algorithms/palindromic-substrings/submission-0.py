class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        # odd
        for i in range(1,n-1):
            l, r = i-1, i+1
            while l>=0 and r<n and s[l]==s[r]:
                res += 1
                l, r = l-1, r+1
        # even
        for i in range(1, n):
            l, r = i-1, i
            while l>=0 and r<n and s[l]==s[r]:
                res += 1
                l, r = l-1, r+1
        return res+n
