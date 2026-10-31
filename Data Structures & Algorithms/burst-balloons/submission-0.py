class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {} # (l, r, ls, rs) => maxcoins
        def dfs(l, r, ls, rs):
            if l>r:
                return 0
            if l==r:
                return (nums[ls] if ls != -1 else 1) * nums[l] * (nums[rs] if rs != -1 else 1)
            if (l, r, ls, rs) in dp:
                return dp[(l, r, ls, rs)]
                
            maxCoins = 0
            for i in range(l, r+1):
                numLs = nums[ls] if ls != -1 else 1
                numRs = nums[rs] if rs != -1 else 1
                maxCoins = max(
                    maxCoins,
                    numLs * nums[i] * numRs + dfs(l, i-1, ls, i) + dfs(i+1, r, i, rs)
                )

            dp[(l, r, ls, rs)] = maxCoins
            return maxCoins

        return dfs(0, len(nums)-1, -1, -1)
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