from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        for i in range(n):
            if nums[i]==val:
                k += 1
                nums[i] = 51
        nums.sort()
        return n-k
