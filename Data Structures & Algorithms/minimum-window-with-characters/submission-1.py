class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def windowValid():
            for keyTrue in freqTrue:
                if freqWindow.get(keyTrue, 0) < freqTrue[keyTrue]:
                    return False
            return True

        freqTrue = {}
        for key in t:
            freqTrue[key] = 1 + freqTrue.get(key, 0)
        
        freqWindow = {}
        l = 0
        
        minL = 0
        minR = len(s)
        for r in range(len(s)):
            freqWindow[s[r]] = 1 + freqWindow.get(s[r], 0)
            while windowValid():
                if r - l + 1 < minR - minL + 1: minL, minR = l, r
                
                freqWindow[s[l]] -= 1
                l += 1
        if minR == len(s) and minL == 0: return ""
        else: return s[minL:minR+1]