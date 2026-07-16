class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        n = len(nums)
        def dfs(i, summ):
            if summ > target or i>n-1: return
            elif summ == target:
                res.append(comb.copy())
            comb.append(nums[i])
            dfs(i, summ+nums[i])

            comb.pop()
            dfs(i+1, summ)
        dfs(0, 0)
        setOfRes = {tuple(x) for x in res}
        cleanRes = [list(x) for x in setOfRes]
        return cleanRes

