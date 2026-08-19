class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxL = 1
        resIdx = [0,0]
        # odd
        for i in range(1,n-1):
            l, r = i-1, i+1
            currMax = 1
            while l>=0 and r<n and s[l]==s[r]:
                currMax+=2
                l, r = l-1, r+1
            if currMax>maxL:
                maxL = currMax
                resIdx = [l+1,r-1]
        # even
        for i in range(1, n):
            l, r = i-1, i
            currMax = 0
            while l>=0 and r<n and s[l]==s[r]:
                currMax+=2
                l, r = l-1, r+1
            if currMax>maxL:
                maxL = currMax
                resIdx = [l+1,r-1]
        res = ""
        l, r = resIdx[0],resIdx[1]
        for i in range(l, r+1):
            res+=s[i]
        return res
