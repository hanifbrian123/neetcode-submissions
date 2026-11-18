class Solution {
    private int[] dp;
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        dp = new int[nums.length];
        Arrays.fill(dp, -1);
        return dfs(0, nums);
    }
    public int dfs(int i, int[] nums) {
        if (i >= nums.length) return 0;
        if (dp[i] != -1) return dp[i];
        dp[i] = Math.max(
            nums[i] + dfs(i+2, nums), dfs(i+1, nums)
        );
        return dp[i];
    }
}