class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = {}
        def dfs(i, j):
            if i>=n or j>=m:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            if text1[i] != text2[j]:
                dp[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            else:
                dp[(i, j)] = 1 + dfs(i+1, j+1)
            return dp[(i, j)]
        return dfs(0, 0)

"""
a c a t
c r a b t


c r a b t
c a t


r a b t k t r 
c a k b t r 

x y z c a a
a c a x z c


c a t


3 + 3*2 + 3*2*1

1, 2, 3

cat
ca
ct
c

at
a

t


crabt

cd
accd

cat




cdafbt
crabt

"""