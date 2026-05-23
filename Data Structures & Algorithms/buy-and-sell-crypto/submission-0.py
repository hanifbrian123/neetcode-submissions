class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        preMax = [0] * len(prices)
        preMax[-1] = prices[-1]
        maxNum = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > maxNum: maxNum = prices[i]
            preMax[i] = maxNum
        
        res = 0
        for i in range(len(prices)-1):
            res = max(preMax[i+1] - prices[i], res)
        return res