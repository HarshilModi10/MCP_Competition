class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(1,len(s)):
            for j in range(len(s)-i):
            
                if s[j] == s[j+i]:
                    dp[j][j+i] = 2 + dp[j+1][j-1+i]
                else:
                    dp[j][j+i] = max(dp[j][j-1+i], dp[j+1][j+i])
        
        return dp[0][-1]