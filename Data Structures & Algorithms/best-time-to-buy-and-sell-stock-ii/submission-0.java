class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int maxBuy = 0; int maxSell = 0;
        for (int i = n-1; i > -1; i--) {
            int maxBuyPrev = maxBuy;
            int maxSellPrev = maxSell;
            maxBuy = Math.max(maxBuy, maxSellPrev - prices[i]);
            maxSell = Math.max(maxSell, prices[i] + maxBuyPrev);
        }
        return maxBuy;
    }
}
