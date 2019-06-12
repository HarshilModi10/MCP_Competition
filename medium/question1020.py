class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        
        count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    temp = self.bfs(A, i,j)
                    if temp > 0:
                        count += temp
        return count
        
    def bfs(self, A, i, j):
        
        if i < 0 or i >= len(A) or j < 0 or j>= len(A[0]):
            return -1
        elif A[i][j] == 0 or A[i][j] == -1:
            return 0
        else:
            A[i][j] = -1
            l = self.bfs(A, i-1, j)
            u = self.bfs(A,i, j-1 )        
            d = self.bfs(A, i, j+1)
            r = self.bfs(A,i+1, j )
            if l == -1 or u == -1 or d == -1 or r == - 1:
                return -1
            else:
                return l+u+r+d+1
            