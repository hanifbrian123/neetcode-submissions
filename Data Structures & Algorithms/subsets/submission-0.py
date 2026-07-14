class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        subset = []
        def backtrack(i):
            if i==n:
                print(f"{i=} {subset=}")
                res.append(subset)
                return
            
            subset.append(nums[i])
            print(subset)
            backtrack(i+1)

            subset.pop()
            print(subset)
            backtrack(i+1)
        backtrack(0)
        return res