class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount+1)]
        dp[amount] = 0
        def dfs(cur):
            if cur > amount: return 10005
            elif dp[cur]!=-1: return dp[cur]

            best = 10005
            for c in coins:
                best = min(best, dfs(cur+c))
            dp[cur] = 1+best
            return 1+best
        res = dfs(0)
        return res if res<10003 else -1