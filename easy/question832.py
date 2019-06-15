class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            l, r = 0, len(A[0])-1
            while l <= r:
                A[i][l], A[i][r] = (1 ^ A[i][r]), (1 ^ A[i][l])
                l += 1
                r -= 1
        return A
        
        