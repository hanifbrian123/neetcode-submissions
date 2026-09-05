class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: 
            return False
        
        n = len(nums)
        total = sum(nums) // 2
        memo = [[None for j in range(total+1)] for i in range(n)]
        
        def dfs(i, cur):
            if i>=n:
                return cur == 0
            elif memo[i][cur] is not None:
                return memo[i][cur]
            elif cur<0:
                return False
            
            memo[i][cur] = dfs(i+1, cur-nums[i]) or dfs(i+1, cur)
            return memo[i][cur]
        return dfs(0, total)