class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        mn, mx = nums[-1], nums[-1]
        res = mx
        for i in range(len(nums)-2, -1, -1):
            cur = nums[i]
            mostLow, mostHigh = (mn, mx) if cur>=0 else (mx, mn)
            
            mn = min(cur, cur*mostLow)
            mx = max(cur, cur*mostHigh)

            res = max(res, mx)
        return res