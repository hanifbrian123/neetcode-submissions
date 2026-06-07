class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for a in nums:
            if mp.get(a, 0):
                return True
            
            mp[a] = 1
        return False