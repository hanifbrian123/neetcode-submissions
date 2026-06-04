from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i])< minLen:
                minLen = len(strs[i])
        ans = ''
        for i in range(minLen):
            a = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i]!=a:
                    return ans
            ans += a
        return ans
