class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        
        for i in range(len(A[0])):
            output = []
            for j in range(len(A)):
                output.append(A[j][i])
            res.append(output)
        
        return res
                
        