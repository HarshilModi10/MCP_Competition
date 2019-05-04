class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # initialize variables
        queue,r,c = [],len(matrix), len(matrix[0])
        
        #modify matrix to zero or infinity 
        for i in range(r):
            for j in range(c):
                # if matrix index is zero keep it zero or make it infinity
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    queue.append((i,j))
        
        #preform bfs from matrix[x][y] equal to zero
        while queue:
            x, y = queue.pop(0)
            neighbour = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
            for row,col in (neighbour):
                val = matrix[x][y] + 1
                #check if neighbours distance is less and if so update and preform BFS
                if 0 <= row < r and 0 <= col < c and val < matrix[row][col]:
                    matrix[row][col] = val
                    queue.append((row,col))
                    
        return matrix
            
                
                    
        