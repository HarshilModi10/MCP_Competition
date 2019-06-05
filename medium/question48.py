class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        
        print matrix
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

#without reverse

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        for x in range(len(matrix)/2):
            row = len(matrix) - 1 - x
            for y in range(x, row):
                col = len(matrix) - 1 - y
                
                #swap the 
                temp = matrix[x][y]
                matrix[x][y] = matrix[col][x]
                matrix[col][x] = matrix[row][col]
                matrix[row][col] = matrix[y][row]
                matrix[y][row] = temp
        return matrix
                