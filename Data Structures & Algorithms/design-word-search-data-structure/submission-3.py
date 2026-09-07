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
        self.cntsearch += 1
        self.wordSearch = word
        self.lenWordSearch = len(word)
        return self.dfs(self.root, 0)
        

    def dfs(self, nodeSrc, i):
        if i>=self.lenWordSearch:
            return nodeSrc.isLeaf

        idx = ord(self.wordSearch[i]) - ord('a')
        if self.wordSearch[i] == '.':
            for child in nodeSrc.childern:
                if child and self.dfs(child, i+1):
                    return True
        elif nodeSrc.childern[idx] and self.dfs(nodeSrc.childern[idx], i+1):
            return True
        
        return False