class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i,j):
            if dp[i][j]:
                return dp[i][j]

            dp[i][j] = 1
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x,y = i+dx,j+dy
                if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(x,y))
            return dp[i][j]

        ret = 0

        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i,j))

        return ret

    # topo sort
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        indegree = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for dx,dy in directions:
                    px,py = i+dx,j+dy
                    if 0<=px<m and 0<=py<n and matrix[px][py] < matrix[i][j]:
                        indegree[i][j] += 1
        
        queue = deque()

        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append([i,j])
        
        maximum = 0

        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in directions:
                    px,py = x+dx,y+dy
                    if 0<=px<m and 0<=py<n and matrix[px][py] > matrix[x][y]:
                        indegree[px][py] -= 1
                        if indegree[px][py] == 0:
                            queue.append([px,py])
            maximum += 1

        return maximum