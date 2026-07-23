class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        k = len(word)
        h = len(board)
        w = len(board[0])
        def dfs(i, j, idxWord, visited):
            if idxWord >= k:
                return True
            if i<0 or i>=h or j<0 or j>=w or board[i][j] != word[idxWord] or (i, j) in visited:
                return False
            visited.add((i, j))
            
            if (dfs(i-1, j, idxWord+1, visited) or dfs(i+1, j, idxWord+1, visited) or dfs(i, j+1, idxWord+1, visited) or dfs(i, j-1, idxWord+1, visited)): 
                return True
            
            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    res = dfs(i, j, 0, set())
                    if res: return True

        return False