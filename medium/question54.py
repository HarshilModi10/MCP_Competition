class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        r, c, x, y = len(matrix), len(matrix[0]), 0, 0
        visited = [False] * (r*c)
        increment = ((1,0), (0,-1), (-1,0), (0,1))
        move = 0
        res = [matrix[0][0]]
        visited[0] = True
        
        while len(res) < r * c:
            local_x = x + increment[move][0]
            local_y = y + increment[move][1]
            
            
            if 0 <= local_x < c and 0 <= local_y < r and not visited[local_y * c + local_x]:
                res.append(matrix[local_y][local_x])
                visited[local_y * c + local_x] = True
                x, y = local_x, local_y
            
            else:
                move = (move+1)%4
        
        return res

    # another version

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        def is_valid_move():
            if 0 <= (row + move[move_index][1]) < max_row and 0 <= (col + move[move_index][0]) <max_col:
                if matrix[row + move[move_index][1]][col + move[move_index][0]] != "X":
                    return True
            return False
        
        if not matrix:
            return []
        
        
        res = [matrix[0][0]]
        matrix[0][0] = "X"
        move = [[1,0], [0, 1], [-1,0], [0,-1]]
        max_row, max_col = len(matrix), len(matrix[0])
        row,col,move_index = 0,0,0
        
        while len(res) != len(matrix[0]*len(matrix)):
            if is_valid_move():
                row = row + move[move_index][1]
                col = col + move[move_index][0]
                res.append(matrix[row][col])
                matrix[row][col] = "X"
            else:
                move_index  = (move_index + 1)%4
        
        return res               
        
        
        
        