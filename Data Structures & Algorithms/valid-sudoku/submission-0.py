class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)

        #Check for cols duplicates
        for col in range(n):
            col_seen = set()
            for row in range(n):
                    value = board[row][col]
                    if value == ".":
                        continue
                    if value in col_seen:
                        return False
                    col_seen.add(value)
            # print(col_seen)

        #Check for row duplication
        for nums in board:
            row_seen = set()
            for r in nums:
                    if r == ".":
                        continue
                    if r in row_seen:
                        return False
                    row_seen.add(r)
            # print(row_seen)
        
        #Check for 3X3 board duplicates
        for start_row in range(0,n,3):
            for start_col in range(0,n,3):
                    board_set = set()
                    for r in range(3):
                        for c in range(3):
                            value = board[start_row+r][start_col+c]
                            if value == ".":
                                continue
                            if value in board_set:
                                return False
                            board_set.add(value)
                            # print(board_set)

        return True
               
        