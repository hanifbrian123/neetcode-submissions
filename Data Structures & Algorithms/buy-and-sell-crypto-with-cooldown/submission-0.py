class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]

        for i in range(n-1, -1, -1):
            bmax, smax = 0, 0
            for j in range(i+1, n):
                bmax = max(
                    bmax, (prices[j] - prices[i]) + dp[j][1]
                )
                if j-i >= 2:
                    smax = max(
                        smax, dp[j][0]
                    )
            dp[i][0], dp[i][1] = bmax, smax
        print(dp)
        return max(x[0] for x in dp)

"""

1 3 4 0 4
-4, 0


    B  S
1:  6, 4
3:  1, 4
4:  0, 0 
0:  4, 0
4: -4, 0
"""