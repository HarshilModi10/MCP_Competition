class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                A[i][j] += min(A[i-1][j and j-1:j+2])
                
        return min(A[-1])