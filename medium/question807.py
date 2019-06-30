class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = [0] * len(grid)
        c = [0] * len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                r[i] = max(r[i], grid[i][j])
                c[j] = max(c[j], grid[i][j])
                
                
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += min(r[i],c[j]) - grid[i][j]
        
        return count
        