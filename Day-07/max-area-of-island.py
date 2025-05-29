from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs solution
        # TC: O(m*n) SC: O(m*n) | m = len(grid) & n = len(grid[0])

        visited = set()
        m,n = len(grid), len(grid[0])

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))

            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            count = 1

            while queue:
                x,y = queue.popleft()

                for dx,dy in directions:
                    px,py = x+dx, y+dy

                    if 0<=px<m and 0<=py<n and (px,py) not in visited and grid[px][py] == 1:
                        queue.append((px,py))
                        visited.add((px,py))
                        count += 1
            
            return count
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, bfs(i,j))
        
        return maxArea

# Union Find solution
# TC: O(m*n) SC: O(m*n)

class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, x, y):
        px,py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[py] > self.rank[px]:
            px,py = py,px
        
        self.parents[py] = px
        self.rank[px] += self.rank[py]
        return True
            
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        land = {}
        root = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land[(i,j)] = root
                    root += 1
        
        dsu = UnionFind(root)

        for x,y in land.keys():
            for dx,dy in directions:
                px, py = x+dx, y+dy
                if 0<=px<m and 0<=py<n and (px,py) in land:
                    dsu.union(land[(x,y)], land[(px,py)])
        
        if not dsu.rank:
            return 0
        
        return max(dsu.rank)



        

        