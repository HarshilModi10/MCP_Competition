class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        c,r = 0,0
        m,n = len(matrix), len(matrix[0])
        diagonal = list()
        
        for _ in range(m*n):
            print(r,c)
            diagonal.append(matrix[r][c])
            
            if (c+r)%2 == 0:
                #going up
                if c == n-1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    c+= 1
                    r -= 1
            else:
                if r == m-1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    c -= 1
                    r += 1
        return diagonal
                    
                    
        