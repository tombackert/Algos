# Time Complexity: O(9^n), n = number of empty cells
# Space Complexity: O(n)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row: int, col: int, digit: str) -> bool:
            # check row
            for j in range(9):
                if board[row][j] == digit:
                    return False

            # check column
            for i in range(9):
                if board[i][col] == digit:
                    return False

            # check sub-box
            sub_box_row = (row // 3) * 3
            sub_box_col = (col // 3) * 3
            for i in range(sub_box_row, sub_box_row+3):
                for j in range(sub_box_col, sub_box_col+3):
                    if board[i][j] == digit:
                        return False

            return True

        def backtrack() -> bool:
            # find next empty cell
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        # try out all possible digits
                        for digit in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if isValid(i, j, digit):
                                board[i][j] = digit
                                if backtrack():
                                    return True
                                board[i][j] = '.'

                        # none of the digits worked, backtrack
                        return False

            # all cells filled, puzzle solved
            return True

        # solve the puzzle
        backtrack()