class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, comb, summ):
            if summ == target:
                res.append(comb.copy())
                return
            if summ > target or i>=n: return

            comb.append(nums[i])
            dfs(i, comb, summ+nums[i])

            comb.pop()
            dfs(i+1, comb, summ)
        dfs(0, [], 0)
        return res