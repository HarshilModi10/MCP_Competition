class Solution(object):
    
    def __init__(self):
        self.total = 0
        
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        r, b = len(grid[0])- 1, len(grid)-1
        
        for i in range(b+1):
            for j in range(r+1):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    self.DFS(grid,i,j,r,b)
                    
        return self.total
        
    
    def DFS(self, grid, i, j, r, b):
        
        sets = [(i + 1,j), (i -1, j), (i,j+1), (i,j -1)]
        
        for num in sets:
            if num[0] < 0 or num[0] > b or num[1] < 0 or num[1] > r:
                self.total += 1
                
            else:
                
                if grid[num[0]][num[1]] == 0:
                    self.total +=  1
            