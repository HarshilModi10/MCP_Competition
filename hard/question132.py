class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp = [[float('inf')] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 0
        
        for i in range(1,len(s)):
            for j in range(len(s) - i):
                k = j + i
                if self.is_palandrome(j,k, s):
                    dp[j][k] = 0
                else:
                    for z in range(j,k):
                        dp[j][k] = min(dp[j][k], 1 + dp[j][z] + dp[z+1][k])
                        
        return dp[0][-1]
    
    def is_palandrome(self, i, k, s):
        
        while i < k:
            if s[i] != s[k]:
                return False
            i+= 1
            k-= 1
        
        return True