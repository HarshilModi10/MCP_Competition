class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = col = False
        
        #check if the first row has a zero
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                row = True
                break
        
        #check if the first column has a zero
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                col = True
                break
        #get the rows and col with zeros
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        #make row zero
        for r in range(1,len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
        
        #make col zero
        for c in range(1,len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0
        
        #make first row to zero
        if row:
            for r in range(len(matrix)):
                matrix[r][0] = 0
                
        #make first col to zero
        if col:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
        return matrix
                
        
        