class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        countDel = 0
        def dfs(l, r):
            nonlocal countDel
            if l>=r:
                return True
            
            if s[l] == s[r]:
                return dfs(l+1, r-1)
            
            countDel += 1
            if countDel >= 2:
                return False
            return dfs(l+1, r) or dfs(l, r-1)
        return dfs(0, len(s)-1)

"""
acdccba


a c b c c b a

acbccba



"""