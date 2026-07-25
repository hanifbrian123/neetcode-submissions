class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def isPalindrome(s):
            n = len(s)
            lastIdx = n-1
            for i in range(n//2):
                if s[i] != s[lastIdx-i]:
                    return False
            return True
        res = []
        def backtrack(i, cur):
            if i>=n:
                idx = 0

                group = []
                isRightSplit = True
                cur.append(n)
                for x in cur:
                    temp = s[idx:x]
                    if isPalindrome(temp):
                        group.append(temp)
                    else:
                        isRightSplit = False
                        break
                    idx = x
                cur.pop()
                if isRightSplit:
                    res.append(group)
                return
            cur.append(i)
            backtrack(i+1, cur)

            cur.pop()
            backtrack(i+1, cur)

        backtrack(1, [])
        return res