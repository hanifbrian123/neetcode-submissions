class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[None for j in range(n)] for i in range(amount)]
        def dfs(i, total):
            if total > amount:
                return 0
            elif total == amount:
                return 1
            elif dp[total][i] is not None:
                return dp[total][i]
            
            dp[total][i] = 0
            for idx in range(i, n):
                dp[total][i] += dfs(idx, total+coins[idx])
            return dp[total][i]
        return dfs(0, 0)
