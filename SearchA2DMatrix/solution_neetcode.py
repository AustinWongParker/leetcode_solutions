class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) # this len(matrix[0]) gets the len of that first list. [1] for second, etc
        top, bot = 0, ROWS - 1

        # the 'first' binary search
        while top <= bot:
            current_row = (top + bot) // 2
            if target > matrix[current_row][-1]: # -1 is end of row
                top = current_row + 1
            elif target > matrix[current_row][0]: # 0 is the beginning of row
                bot = current_row -1
            else:
                break
        
        # if it goes through top and bottom rows of matrix and doesnt find it, return false
        if not (top <= bot):
            return False
        current_row = (top + bot) // 2
        left, right = 0, COLS - 1

        # the 'second' binary search
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[current_row][middle]:
                left = middle + 1
            elif target < matrix[current_row][middle]:
                right = middle -1
            else:
                 # cannot find target value
                return False
        return True