class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        res = 1
        for i in range(n-1, -1, -1):
            mx = 0
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    mx = max(dp[j], mx)
            dp[i] = dp[i] + mx
            res = max(dp[i], res)
        return res
        
