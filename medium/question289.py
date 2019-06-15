class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbours = self.count(board,i+1,j) + self.count(board,i-1,j) + self.count(board,i,j-1) + self.count(board,i,j+1) + self.count(board,i+1,j+1) + self.count(board,i+1,j-1) + self.count(board,i-1,j+1) + self.count(board,i-1,j-1)
                
                if board[i][j] == 1:
                    if 2 <= live_neighbours <= 3:
                        board[i][j] += 2
                else:
                    if live_neighbours == 3:
                        board[i][j] += 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] >> 1
        
        return board
    
    def count(self, board, i, j):
        if 0 <= i < len(board) and 0<= j < len(board[0]):
            return 1 & board[i][j]
        return 0
        
                        
                