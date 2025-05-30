class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs over every point -- better way to do this in retrospect is to start at solutions and work backwards 
        # TC: O((m*n)^2) SC: O(m*n)

        m,n = len(heights), len(heights[0])
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited = set()
            visited.add((i,j))
            pac, atl = False, False

            while queue:
                x,y = queue.popleft()

                if x == 0 or y == 0:
                    pac = True
                
                if x == m-1 or y == n-1:
                    atl = True
                
                if pac and atl:
                    return True

                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    px,py = x+dx, y+dy

                    if 0<=px<m and 0<=py<n and (px,py) not in visited and heights[px][py] <= heights[x][y]:
                        queue.append((px,py))
                        visited.add((px,py))
                    
            return atl and pac

        ret = []

        for i in range(m):
            for j in range(n):
                if bfs(i,j):
                    ret.append([i,j])
            
        return ret
        