class Node:
    def __init__(self, c):
        self.childern = [None for i in range(26)]
        self.isLeaf = False
        self.c = c
class WordDictionary:

    def __init__(self):
        self.root = Node(None)
        
        self.wordSearch = None
        self.lenWordSearch = None
        self.searchIsFalse = False

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.childern[idx]:
                new = Node(c)
                cur.childern[idx] = new
                cur = new
            else:
                cur = cur.childern[idx]
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        self.wordSearch = word
        self.lenWordSearch = len(word)
        self.searchIsFalse = False
        ret = self.dfs(self.root, 0)
        return ret if not self.searchIsFalse else False
    def dfs(self, nodeSrc, i):
        if i>=self.lenWordSearch:
            return nodeSrc.isLeaf
        
        if self.wordSearch[i] == '.':
            for child in nodeSrc.childern:
                if child:
                    res = self.dfs(child, i+1)
                    if res:
                        return True
        else:
            idx = ord(self.wordSearch[i]) - ord('a')
            if not nodeSrc.childern[idx]:
                self.searchIsFalse = True
                return False
            res = self.dfs(nodeSrc.childern[idx], i+1)
            if res:
                return True
        
        
        return False

