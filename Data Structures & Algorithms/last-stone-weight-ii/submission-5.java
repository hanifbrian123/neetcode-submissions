class Solution {
    private int target;
    private int[] stones;
    private int[][] dp;
    private int sumStones;
    public int lastStoneWeightII(int[] stones) {
        int sumStones = Arrays.stream(stones).sum();
        this.sumStones = sumStones;
        this.target = sumStones / 2;
        this.stones = stones;
        this.dp = new int[stones.length][target + 1];
        for (int[] row: dp) {
            Arrays.fill(row, -1);
        }
        return dfs(0, 0);
    }
    private int dfs(int i, int total) {
        if (total >= target || i >= stones.length) return Math.abs(
            (sumStones - total) - total
        );
        
        if (dp[i][total] != -1) return dp[i][total];
        
        dp[i][total] = Math.min(dfs(i + 1, total + stones[i]), dfs(i + 1, total));
        return dp[i][total];        
    }
}