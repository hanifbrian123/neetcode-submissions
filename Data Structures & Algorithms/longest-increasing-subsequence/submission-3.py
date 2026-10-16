class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)-1, -1, -1):
            max_increasing = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    max_increasing = max(max_increasing, dp[j])
            dp[i] = dp[i] + max_increasing
            res = max(dp[i], res)
        return res