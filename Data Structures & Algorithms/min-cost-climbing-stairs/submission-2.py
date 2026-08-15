class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1 for i in range(n)]
        def dfs(i):
            if i>=n: return 0
            elif cache[i] != -1: return cache[i]
            curcost = cost[i] if i>=0 else 0
            cache[i] = curcost + min(dfs(i+1), dfs(i+2))
            return cache[i]
        return dfs(-1)
