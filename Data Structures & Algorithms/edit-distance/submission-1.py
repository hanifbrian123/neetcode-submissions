class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {} # (i, j)
        n, m = len(word1), len(word2)
        def dfs(i, j):
            if i >= n and j >= m:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            
            if i >= n:
                dp[(i, j)] = 1 + dfs(i, j+1)
            elif j >= m:
                dp[(i, j)] = 1 + dfs(i+1, j)
            elif word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
            else:
                dp[(i, j)] = 1 + min(
                    dfs(i+1, j+1),
                    dfs(i, j+1),
                    dfs(i+1, j),
                )
            return dp[(i, j)]
        return dfs(0, 0)
            
"""
=> I ~1h20m nyelesaiin ini :(
n e t c d e e
n e e t c o d e

m o n k e y s
m o n e y

. => REPLACE => i+1, j+1
, => INSERT => i, j+1
/ => REMOVE => i+1, j

n e t c d e e e e e e
n e e t c o d e

n e _ t c d e
n e e t c o d e

c c a t
c a t



c r r r r t b a _
c _ _ _ _ _ _ a t

c r r r r t b a _ k
c _ _ _ _ _ _ a t k

c _ r r r t b a _ k
c a _ _ _ t _ _ _ k

=> 7
"""