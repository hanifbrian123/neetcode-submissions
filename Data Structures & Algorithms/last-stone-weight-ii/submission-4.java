class Solution {
    private int target;
    private int[] stones;
    private int[][] dp;
    public int lastStoneWeightII(int[] stones) {
        int sumStones = Arrays.stream(stones).sum();
        this.target = sumStones / 2;
        this.stones = stones;
        this.dp = new int[stones.length][target + 1];
        for (int[] row: dp) {
            Arrays.fill(row, -1);
        }
        int half = dfs(0, 0);
        return Math.abs(half - (sumStones - half));
    }
    private int dfs(int i, int total) {
        if (total >= target || i >= stones.length) return total;
        if (dp[i][total] != -1) return dp[i][total];

        int res1 = dfs(i + 1, total + stones[i]);
        int res2 = dfs(i + 1, total);
        if (Math.abs(res1 - target) <= Math.abs(res2 - target)) {
            return res1;
        } else {
            return res2;
        }
    }
}



// 10 12 30