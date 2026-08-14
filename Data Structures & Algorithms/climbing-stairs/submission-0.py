class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(total):
            if total == n:
                return 1
            elif total>n:
                return 0
            elif total in memo:
                return memo[total]
            res = dfs(total+1) + dfs(total+2)
            memo[total] = res
            return res
        return dfs(0)
            