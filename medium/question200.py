class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        move = ((1,0),(0,1), (-1,0), (0,-1))                           
        
        for r in range(len(grid)):
            for c in range (len(grid[0])):    
                
                if grid[r][c] == "1":
                    count += 1
                    self.bfs(grid, r,c,move)   
        
        return count

            
    def bfs(self,grid, r, c,move):            
        grid[r][c] = "#"
        for mv in move:
            row = r + mv[0]
            col = c + mv[1]
            print(row, col)
                
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
                self.bfs(grid,row,col,move)   
        