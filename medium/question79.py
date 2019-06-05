class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.bfs(board, word, i,j):
                    return True
        return False
    
    def bfs(self, board, word, i, j):
        if not word:
            return True
        
        if 0<= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
            temp = board[i][j]
            board[i][j] = "#"
            res = self.bfs(board, word[1:], i+1, j) or self.bfs(board, word[1:], i-1, j) or self.bfs(board, word[1:], i, j+1) or self.bfs(board, word[1:], i, j-1)
            board[i][j] = temp
            return res
        return False
                
            
        