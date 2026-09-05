class PrefixTree:

    def __init__(self):
        self.childern = [None for i in range(26)]
        self.isEndOfWord = False

    def insert(self, word: str) -> None:
        curp = self
        for c in word:
            index = ord(c)-ord('a')
            nextp = curp.childern[index]
            if nextp is None:
                nextp = PrefixTree()
                curp.childern[index] = nextp
            curp = nextp
        curp.isEndOfWord = True


    def search(self, word: str) -> bool:
        curp = self
        for c in word:
            index = ord(c)-ord('a')
            nextp = curp.childern[index]
            if not nextp:
                return False
            curp = nextp
        return curp.isEndOfWord
            

    def startsWith(self, prefix: str) -> bool:
        curp = self
        for c in prefix:
            index = ord(c)-ord('a')
            nextp = curp.childern[index]
            if not nextp:
                return False
            curp = nextp
        return True
        