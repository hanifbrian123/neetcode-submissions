class Solution {
    private int[][][] dp;
    public int stoneGameII(int[] piles) {
        dp = new int[piles.length][2][piles.length + 1];
        for (int[][] row1: dp) {
            for (int[] row2: row1) {
                Arrays.fill(row2, -1);
            }
        }
        return dfs(0, true, 1, piles);
    }
    private int dfs(int idx, boolean alice, int m, int[] piles) {
        if (idx >= piles.length) return 0;
        if (dp[idx][ (alice) ? 0 : 1 ][m] != -1) return dp[idx][ (alice) ? 0 : 1 ][m];

        int maxX = 2*m;
        
        if (alice) {
            int curTotal = 0;
            int res = Integer.MIN_VALUE;
            for (int i = idx; i < idx + maxX && i < piles.length; i++) {
                curTotal += piles[i];
                res = Math.max(res, curTotal + dfs(i + 1, !alice, Math.max(i - idx + 1, m), piles));
            }
            dp[idx][0][m] = res;
            return res;
        } else {
            int res = Integer.MAX_VALUE;
            for (int i = idx; i < idx + maxX && i < piles.length; i++) {
                res = Math.min(res, dfs(i + 1, !alice, Math.max(i - idx + 1, m), piles));
            }
            dp[idx][1][m] = res;
            return res;
        }

    }
}


// 3 1 2 5 7


// alice turn:
//     now take + dfs()
// bob turn:
//     dfs()