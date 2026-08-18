class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.nums = nums
        return max(nums[0], self.bottomUp(0,n-1), self.bottomUp(1,n))

    def bottomUp(self, s, e):
        max1, max2 = 0, 0
        for i in range(s, e):
            temp = max(max1, max2)
            max1 = max2+self.nums[i]
            max2 = temp
        return max(max1, max2)
