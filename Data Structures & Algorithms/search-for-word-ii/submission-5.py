class TrieNode:
    def __init__(self, ch=None):
        self.childern = [None for i in range(26)]
        self.ch = ch
class Tries:
    def __init__(self, board, maxLen):
        self.root = TrieNode()
        self.board = board
        self.maxLen = maxLen
        self.build()
    def build(self):
        n = len(self.board)
        m = len(self.board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j, src, cnt, visited):
            idx = ord(self.board[i][j]) - ord('a')
            if not src.childern[idx]:
                newNode = TrieNode(self.board[i][j])
                src.childern[idx] = newNode
            
            src = src.childern[idx]
            cnt+=1
            visited.add((i, j))
            for d in directions:
                iAdj, jAdj = i+d[0], j+d[1]
                if (
                    iAdj < 0 or jAdj < 0 or iAdj >= n or jAdj >= m 
                    or (iAdj, jAdj) in visited or cnt==self.maxLen
                ):
                    continue
                dfs(iAdj, jAdj, src, cnt, visited)
                visited.remove((iAdj, jAdj))

        for i in range(n):
            for j in range(m):
                dfs(i, j, self.root, 0, set())

    def search(self, word):
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.childern[idx]:
                return False
            cur = cur.childern[idx]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        maxLen = max(len(w) for w in words)
        
        # Build Tries
        tr = Tries(board, maxLen)
        # tr.display()
        
        # Search each word in the tries
        res = []
        for w in words:
            if tr.search(w):
                res.append(w)
        return res