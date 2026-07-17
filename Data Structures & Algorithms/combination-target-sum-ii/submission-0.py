class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def backtrack(i, curComb, curSum):
            if curSum == target:
                res.append(curComb.copy())
                return
            if curSum > target or i >= n: return

            curComb.append(candidates[i])
            backtrack(i+1, curComb, curSum+candidates[i])

            curComb.pop()
            backtrack(i+1, curComb, curSum)
        backtrack(0, [], 0)
        
        for x in res:
            x.sort()
        setOfRes = {tuple(x) for x in res}
        resClean = [list(x) for x in setOfRes]
        return resClean