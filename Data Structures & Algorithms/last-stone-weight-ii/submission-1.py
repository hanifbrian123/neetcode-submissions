class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStones = sum(stones)
        target = sumStones // 2
        n = len(stones)
        dp = {}
        def dfs(i, total):
            if i>=n or total>=target:
                return abs(total-(sumStones-total))
            elif (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(
                dfs(i+1, total+stones[i]), dfs(i+1, total)
            )
            return dp[(i, total)]
        return dfs(0, 0)

"""
4,4,1,7,10 => 13
"""