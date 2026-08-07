class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            if i<0 or i>=n or j<0 or j>=m or board[i][j] == 'X' or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)


        visited = set()
        # top bottom
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)
        # side
        for i in range(1, n-1):
            dfs(i, 0)
            dfs(i, m-1)

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    board[i][j] = "X"
                    