class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m,n = len(board), len(board[0])

        queue = deque()
        marked = set()

        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i,0))
                marked.add((i,0))
            if board[i][n-1] == 'O':
                queue.append((i,n-1))
                marked.add((i,n-1))
            
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0,j))
                marked.add((0,j))
            if board[m-1][j] == 'O':
                queue.append((m-1,j))
                marked.add((m-1,j))
        
        while queue:
            x,y = queue.popleft()

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                px,py = x+dx,y+dy

                if 0<=px<m and 0<=py<n and board[px][py] == 'O' and (px,py) not in marked:
                    queue.append((px,py))
                    marked.add((px,py))
                    
        for i in range(m):
            for j in range(n):
                if (i,j) not in marked:
                    board[i][j] = 'X'
        



        