class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)

        #Create dict of set for rows, cols and squares
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        #Loop through rows and cols
        for r in range(n):
            for c in range(n):
                #Create a value var to store board values
                value = board[r][c]

                #Check if there is an empty value in the board
                if value == ".":
                    continue
                
                #Check for duplicates in the sets
                if (value in row_set[r] or
                    value in col_set[c] or
                    value in square_set[(r//3,c//3)]):
                    return False
                
                #Add values to the sets
                row_set[r].add(value)
                col_set[c].add(value)
                square_set[(r//3,c//3)].add(value)

        return True
               
        