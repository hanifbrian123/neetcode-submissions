class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in window:
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            res = max(res, r - l + 1)
        return res
