class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: return 0
        minA = prices[0]
        maxP = 0
        for i in range(1, len(prices)):
            maxP = max(prices[i]-minA, maxP)
            if prices[i] < minA:
                minA = prices[i]
        return maxP