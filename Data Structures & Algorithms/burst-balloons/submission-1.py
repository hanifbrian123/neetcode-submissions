class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {} # (l, r) => maxcoins
        n = len(nums)
        def dfs(l, r):
            if l>r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
                
            maxCoins = 0
            for i in range(l, r+1):
                numsLs = nums[l-1] if l-1 >= 0 else 1
                numsRs = nums[r+1] if r+1 < n else 1
                maxCoins = max(
                    maxCoins,
                    numsLs * nums[i] * numsRs + dfs(l, i-1) + dfs(i+1, r)
                )

            dp[(l, r)] = maxCoins
            return maxCoins

        return dfs(0, n-1)
"""
4 2 3 7

[4] 2 3 7 => l=0, r=3
LEFT: l=0, r=-1
    l=-1
    r=-1




4,2,[3],7 => 1 * 3 * 1
    [4],2 => 1 * 4 * 3
        [2] => 4 * 2 * 3
    4,[2] => 1 * 2 * 3
        [4] => 1 * 4 * 2
    
    [7] => 3 * 7 * 1

n * n - 1 * n - 2 * .....
n!


4*2*3=>24
4*3*7=>84
1*4*7=>28
1*7*1=>7
=>143



7
2,3,7=>42
4,2,7=>56
1,4,7=>28
1,7,1=>7



"""