class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
        uniqNums = list(set(nums))
        res = []
        n = len(uniqNums)
        def dfs(i, cur):
            if i>=n: 
                res.append(cur.copy())
                return
            cur.append(uniqNums[i])
            freq[uniqNums[i]] -= 1
            if freq[uniqNums[i]] > 0:
                dfs(i, cur)
            else:
                dfs(i+1, cur)
            
            cur.pop()
            freq[uniqNums[i]] += 1
            dfs(i+1, cur)
        dfs(0, [])
        return res