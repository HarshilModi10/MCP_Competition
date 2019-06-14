class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 and n==1:
            return 1
        
        dp = [[None for i in range(m)] for j in range(n)]
        dp[0][0] = 0
        if n > 1:
            dp[1][0] = 1
        if m > 1:
            dp[0][1] = 1
        return self.num_unique_paths(m,n,dp)
    
    def num_unique_paths(self, m, n, dp):
        if m == 0 or n == 0:
            return 0
        
        if dp[n-1][m-1] != None:  
            return dp[n-1][m-1]
        
        total = self.num_unique_paths(m-1, n, dp) + self.num_unique_paths(m, n-1, dp)
        dp[n-1][m-1] = total
        return total
        
        
        
        