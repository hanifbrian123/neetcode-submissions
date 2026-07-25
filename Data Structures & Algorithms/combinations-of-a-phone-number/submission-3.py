class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        mp = {
            '2': ['a', 'b','c'],
            '3': ['d', 'e','f'],
            '4': ['g', 'h','i'],
            '5': ['j', 'k','l'],
            '6': ['m', 'n','o'],
            '7': ['p', 'q','r','s'],
            '8': ['t', 'u','v'],
            '9': ['w', 'x','y','z'],
        }
        n = len(digits)
        def backtrack(i, cur):
            if i>=n:
                curstr = "".join(cur)
                res.append(curstr)
                return
            for x in mp[digits[i]]:
                cur.append(x)
                backtrack(i+1, cur)

                cur.pop()
        backtrack(0, [])
        return res
