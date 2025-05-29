from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs solution 
        # TC: O(m*n) SC: O(min(m,n))
        m,n = len(grid), len(grid[0])
        visited = set()

        def bfs(i,j):
            if (i,j) in visited:
                return 0

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))

            while queue:
                x,y = queue.popleft()

                for dx,dy in directions:
                    nx, ny = x+dx, y+dy
                    if (nx,ny) not in visited and 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        queue.append((nx,ny))
                        visited.add((nx,ny))
            
            return 1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += bfs(i,j)
        
        return count
                
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs solution
        # TC: O(m*n) SC: O(m*n)

        m,n = len(grid), len(grid[0])

        visited = set()
        def dfs(i,j):
            if (i,j) in visited or i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return 0

            visited.add((i,j))

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
        
        return count


# Union Find solution
# TC: O(m*n) SC: O(m*n)

class UnionFind:
    # for union find problems u have to make your own data structure
    def __init__(self, grid):
        m,n = len(grid), len(grid[0])
        # every time you make parents list, with each position representing unique components 
        self.parents = []
        # (rank list is optional for efficiency)
        self.rank = []
        self.components = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # here we define a component as a number in this array (each component having their own unique number to begin with)
                    self.parents.append(i * n + j)
                    self.components += 1
                else:
                    # if it isn't meant to be a component we can put a dummy value (just so the indexing works for the proper components)
                    self.parents.append(-1)
                # default rank is 1
                self.rank.append(1)
    
    # find is a default method you make everytime
    def find(self, i):
        # this if here is called path compression (speeds up later computations)
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        # this will tell you the root of the component 
        # ex: node 2 and 5 are merged so parent list would be like this [0,1,2,3,4,2]
        # since node 5 has value 2 it would move down
        return self.parents[i]
    
    # union is a default method you make everytime
    def union(self, x, y):
        # rx and ry find the roots
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            # comparing rank is for efficiency (merging components based on which one is bigger so we dont have to change as many roots)
            if self.rank[rx] < self.rank[ry]:
                rx, ry = ry, rx
            
            # so this now says that the nodes are merged (in the same component)
            self.parents[ry] = rx
            # rank for this node will tell you how many nodes are in this component
            self.rank[rx] += self.rank[ry]
            self.components -= 1
    
    def getComponents(self):
        return self.components
        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        dsu = UnionFind(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dx, dy in directions:
                        nx,ny = i+dx, j+dy

                        if 0<=nx<m and 0<=ny<n and grid[nx][ny] == '1':
                            dsu.union(nx*n+ny, i*n+j)

        return dsu.getComponents()


        

    