class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        half = len(nums) // 2
        for num in freq:
            if freq[num] > half:
                return num