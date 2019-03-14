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
        