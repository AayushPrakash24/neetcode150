class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # matrix transpose then reverse
        # TC: O(n^2) SC: O(1)

        n = len(matrix)

        # transpose operation
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse operation
        for row in matrix:
            l, r = 0, n-1
            while l <= r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1

        # this does the same thing as the reverse operation (putting [::-1] reverses a list)
        # for r in range(n):
        #     matrix[r] = matrix[r][::-1]