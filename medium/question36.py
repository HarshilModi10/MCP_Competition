class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check if the rows are valid
        valid_row = self.check_valid_row(board)
        
        #check if the columns are valid
        valid_column = self.check_valid_col(board)
        
        #check if the sub box are valid
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.check_valid_box(board, i, j):
                    return False

        
        return valid_row and valid_column

    
    def check_valid_row(self, board):
        
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in visited:
                        return False
                    visited.add(board[i][j])
        return True
    
    def check_valid_col(self, board):
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in visited:
                        return False
                    visited.add(board[j][i])
        return True
    
    def check_valid_box(self, board, r, c):
        visited = set()
        for i in range(r, r+3):
            for j in range(c, c+3):
                if board[i][j] != ".":
                    if board[i][j] in visited:
                        return False
                    visited.add(board[i][j])
        return True
        