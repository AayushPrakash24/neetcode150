class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        w = len(word)

        if m * n == 1:
            return board[0][0] == word

        def backtrack(board,x,y,i):
            if i >= w:
                return True
            
            if board[x][y] == word[i]:
                board[x][y] = '#'
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    px,py = x+dx,y+dy
                    if 0<=px<m and 0<=py<n:
                        if backtrack(board, px, py, i+1):
                            return True
                board[x][y] = word[i]
            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(board, i, j, 0):
                    return True
        return False

            