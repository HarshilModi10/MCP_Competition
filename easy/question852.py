class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(0,len(A)-2):
            if A[i] < A[i+1] and A[i+1] > A[i+2]:
                return i+1