class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) 
        rows = collections.defaultdict(set) 
        grid = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in grid[(r // 3, c // 3)]):
                    return False
                     # the current row in our rows hashset will return true for the if conditional AKA the number is in the row
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])
        return True

        
