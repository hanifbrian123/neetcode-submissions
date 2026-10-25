class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)
        def dfs(i, total):
            if i >= n:
                if total == target:
                    return 1
                else:
                    return 0
            elif (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
            return dp[(i, total)]
        return dfs(0, 0)
