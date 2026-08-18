class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # self.nums = nums
        return max(nums[0], self.bottomUp(0,n-1, nums), self.bottomUp(1,n, nums))

    def bottomUp(self, s, e, nums):
        max1, max2 = 0, 0
        for i in range(s, e):
            temp = max(max1, max2)
            max1 = max2+nums[i]
            max2 = temp
        return max(max1, max2)
