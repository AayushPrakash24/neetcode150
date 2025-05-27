class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sets and index math
        # TC: O(1) SC: O(1)
    
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in rows[i] or val in cols[j] or val in boxes[i//3 * 3 + j//3]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[i//3*3+j//3].add(val)

        return True