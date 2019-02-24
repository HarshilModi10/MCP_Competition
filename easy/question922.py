class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even,odd,n = 0, 1, len(A)
        
        while even < n and odd < n:
            if A[even] %2 and not A[odd] %2:
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2
            elif A[even] %2 == 0:
                even += 2
            elif A[odd] %2 == 1:
                odd += 2
        
        return A
            
        