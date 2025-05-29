class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        oranges = 0
        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))

        time = 0
        
        while queue and oranges != 0:
            
            for _ in range(len(queue)):
                x,y = queue.popleft()

                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    px,py = x+dx, y+dy
                    if 0<=px<m and 0<=py<n and (px,py) not in visited and grid[px][py] == 1:
                        queue.append((px,py))
                        visited.add((px,py))
                        oranges -= 1
            time += 1

        if oranges == 0:
            return time
        return -1
                        


        