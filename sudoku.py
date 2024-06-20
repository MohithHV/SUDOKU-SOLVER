class SudokuSolver:
    def _init_(self, board):
        self.board = board
        self.size = 9  # Size of the Sudoku board
        self.empty = 0  # Placeholder for empty cells

    def solve(self):
        # Function to solve the Sudoku puzzle
        if not self._solve():
            print("No solution exists.")
        else:
            self._print_board()

    def _solve(self):
        # Helper function using backtracking to solve Sudoku
        row, col = self._find_empty()
        
        if row is None:
            return True  # Puzzle solved successfully
        
        # Try filling the empty cell with values 1 to 9
        for num in range(1, self.size + 1):
            if self._is_valid(row, col, num):
                self.board[row][col] = num
                
                if self._solve():
                    return True
                
                # Backtrack
                self.board[row][col] = self.empty
        
        return False  # Trigger backtracking

    def _find_empty(self):
        # Find an empty cell in the board (represented by 0)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == self.empty:
                    return i, j
        return None, None  # No empty cell found

    def _is_valid(self, row, col, num):
        # Check if it's valid to place 'num' in board[row][col]
        return (self._is_valid_row(row, num) and
                self._is_valid_col(col, num) and
                self._is_valid_box(row - row % 3, col - col % 3, num))

    def _is_valid_row(self, row, num):
        # Check if 'num' is not already present in the row
        return num not in self.board[row]

    def _is_valid_col(self, col, num):
        # Check if 'num' is not already present in the column
        for i in range(self.size):
            if self.board[i][col] == num:
                return False
        return True

    def _is_valid_box(self, start_row, start_col, num):
        # Check if 'num' is not already present in the 3x3 box
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def _print_board(self):
        # Print the solved Sudoku board
        for row in self.board:
            print(" ".join(map(str, row)))


# Example usage:
if  __name__ == "_main_":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    solver = SudokuSolver(board)
    solver.solve()