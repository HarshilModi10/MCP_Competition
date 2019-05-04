class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        self.friends = set()
        
        for i in range(len(M)):
            if i not in self.friends:
                count += 1
                self.dfs(i,M)
                
        return count
        
    def dfs(self,i, M):
        
        for j in range(len(M)):            
            if j not in self.friends and M[i][j] == 1:
                self.friends.add(j)
                self.dfs(j,M)
                
            