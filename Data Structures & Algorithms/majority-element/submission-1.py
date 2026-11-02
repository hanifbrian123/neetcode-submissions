class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] != res:
                count -= 1
            if count == 0:
                res, count = nums[i], 1
        return res
