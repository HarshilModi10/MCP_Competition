class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            dp[i][0] = i
        for j in range(len(word1)+1):
            dp[0][j] = j
        
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word2[i] == word1[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1 + min(dp[i+1][j], dp[i][j+1])
                    
        return dp[-1][-1]
        