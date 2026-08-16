class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        for i in range(len(nums)-1, -1, -1):
            temp = max2+nums[i]
            max2 = max(max1, max2)
            max1 = temp
        return max(max1, max2)