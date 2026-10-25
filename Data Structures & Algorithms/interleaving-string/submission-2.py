class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1==0 and l2==0 and l3==0:
            return True
        
        falseSet = set()
        def dfs(i, j, k):
            if k>=l3 and i>=l1 and j>=l2:
                return True
            if k>=l3 and (i<l1 or j<l2):
                return False
            if k<l3 and (i>=l1 and j>=l2):
                return False
            
            if (i, j) in falseSet:
                return False

            if i<l1 and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    return True
            
            if j<l2 and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    return True

            falseSet.add((i, j))

            return False
        return dfs(0, 0, 0)
"""
aaaaa
bbabb
aabbaabbaa
"""





# [a a a a] a
# [b b] a b b

# [a a a] a a
# [b b a] b b

# [a a b b a a] b b a a


# a a a a


# a b c
# a y z
# a b x z c y