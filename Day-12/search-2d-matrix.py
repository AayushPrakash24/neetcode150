class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l,r = 0, m*n-1

        while l<=r:
            mid = l + (r-l)//2
            x,y = divmod(mid, n)

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
            

    