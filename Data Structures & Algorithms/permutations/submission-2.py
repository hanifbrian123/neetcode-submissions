class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permu = []
        def dfs(curSet: Set[int]):
            leaf = True
            for x in nums:
                if x not in curSet:
                    leaf = False
                    curSet.add(x)
                    permu.append(x)
                    dfs(curSet)
                    
                    permu.pop()
                    curSet.remove(x)
            if leaf:
                res.append(permu.copy())
        dfs(set())
        return res

