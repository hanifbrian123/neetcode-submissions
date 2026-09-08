class Solution:
    def __init__(self):
        self.curw = None
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = []

        def dfs(i, j, wIdx):
            # print()
            # print("+"*20)
            # print(i, j, wIdx)
            if wIdx >= len(self.curw):
                # print(f"TRUEEE: {(i, j, wIdx)}")
                return True
            # print(f"{self.curw[wIdx]=}")
            # if not (i<0 or j<0 or i>=n or j>=m):
                # print(f"{board[i][j]}")
            if i<0 or j<0 or i>=n or j>=m or self.curw[wIdx] != board[i][j] or (i, j) in visited:
                return False
            
            visited.add((i, j))
            for d in directions:
                i_adj, j_adj = i+d[0], j+d[1]
                if dfs(i_adj, j_adj, wIdx+1):
                    return True
            return False

        for w in words:
            self.curw = w
            doneForCurWord = False
            for i in range(n):
                for j in range(m):
                    visited = set()
                    if dfs(i, j, 0):
                        res.append(w)
                        doneForCurWord = True
                    if doneForCurWord:
                        break
                
                if doneForCurWord:
                        break
        return res