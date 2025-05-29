class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # pop segments of matrix solution
        # TC: O(m*n) SC: O(m*n)

        # given matrix = [[1,2,3],[4,5,6],[7,8,9]]
        # first pop first row [1,2,3]
        # second pop last column [6, 9]
        # third pop bottom row reverse order [7,8] -> [8,7]
        # fourth pop first column reverse order [4] -> [4]
        # repeat algo until ans == |m*n| or matrix don't exist (if using popping)

        ans = []

        while matrix:
            ans.extend(matrix.pop(0))

            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())
            
            if matrix:
                ans.extend(matrix.pop()[::-1])
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        
        return ans

