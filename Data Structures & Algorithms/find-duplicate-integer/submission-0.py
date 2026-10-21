class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setnum = set()
        for n in nums:
            if n in setnum:
                return n
            setnum.add(n)