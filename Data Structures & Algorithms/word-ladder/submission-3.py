class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isValidT(a, b):
            cntFalse = 0
            for i in range(len(a)):
                if a[i] != b[i]: cntFalse+=1
            return cntFalse == 1

        q = collections.deque([beginWord])
        visited = {beginWord}
        lv = 1
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node == endWord:
                    return lv
                for w in wordList:
                    if isValidT(node, w) and w not in visited:
                        visited.add(w)
                        q.append(w)
            lv+=1
        return 0