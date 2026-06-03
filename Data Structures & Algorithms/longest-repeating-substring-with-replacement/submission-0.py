class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def keyWithMaxV(mp: dict):
            maxV = None
            keyMax = None
            for key in mp:
                if maxV is None and keyMax is None:
                    maxV = mp[key]
                    keyMax = key
                else:
                    if mp[key] > maxV:
                        maxV = mp[key]
                        keyMax = key
            return keyMax
        l = 0
        maxL = 0
        mp = {key:0 for key in set(s)}
        for r in range(len(s)):
            # print(r, l)
            mp[s[r]] += 1
            while (r-l+1) - mp[keyWithMaxV(mp)] > k:
                mp[s[l]] -= 1
                l+=1
                # print(mp)
                # print(l)
            maxL = max((r-l+1), maxL)
        return maxL
