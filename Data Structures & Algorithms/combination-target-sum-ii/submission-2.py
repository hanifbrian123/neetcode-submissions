class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        freq = {}
        for x in candidates:
            freq[x] = 1 + freq.get(x, 0)
        setCandidates = list(set(candidates))
        
        n = len(setCandidates)
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i>=n or total>target: return
            
            cur.append(setCandidates[i])
            freq[setCandidates[i]] -= 1
            if freq[setCandidates[i]] > 0:
                dfs(i, cur, total+setCandidates[i])
            else:
                dfs(i+1, cur, total+setCandidates[i])

            cur.pop()
            freq[setCandidates[i]] += 1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res



