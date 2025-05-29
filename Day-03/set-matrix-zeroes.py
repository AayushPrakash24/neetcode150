class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # mark spots with temporary hashes and then correct later
        # TC: O(m*n) SC: O(1)
        
        m,n = len(matrix), len(matrix[0])

        def mark(i,j):
            for k in range(m):
                if matrix[k][j] != 0:
                    matrix[k][j] = '#'
            
            for k in range(n):
                if matrix[i][k] != 0:
                    matrix[i][k] = '#'

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    mark(i,j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0