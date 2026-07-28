class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(i, cur, visited, rightBotDiagonal, leftBotDiagonal):
            if i >= n:
                res.append(cur.copy())
            
            for j in range(n):
                if j in visited or i-j in rightBotDiagonal or i+j in leftBotDiagonal:
                    continue
                cur.append(j)
                visited.add(j)
                rightBotDiagonal.add(i-j)
                leftBotDiagonal.add(i+j)
                backtrack(i+1, cur, visited, rightBotDiagonal, leftBotDiagonal)

                cur.pop()
                visited.remove(j)
                rightBotDiagonal.remove(i-j)
                leftBotDiagonal.remove(i+j)

        backtrack(0, [], set(), set(), set())
        print(res)
        resStr = []


        for x in res:
            temp = []
            for idx in x:
                # make str
                s = ""
                for i in range(n):
                    s += '.' if i!=idx else 'Q'
                temp.append(s)
            resStr.append(temp)
        return resStr
            