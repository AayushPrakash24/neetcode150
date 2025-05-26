from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # bfs solution
        # TC: O(m*n) SC: O(m*n)
        m,n = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j,1))
                    visited.add((i,j))
                elif rooms[i][j] == -1:
                    visited.add((i,j))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            i,j,step = queue.popleft()

            for di,dj in directions:
                pi, pj = i+di, j+dj

                if 0<=pi<m and 0<=pj<n and (pi,pj) not in visited:
                    rooms[pi][pj] = step
                    visited.add((pi,pj))
                    queue.append((pi,pj,step+1))
        






        
        