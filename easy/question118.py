class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        
        if numRows == 0:
            return []
        
        if numRows >= 1:
            res.append([1])
        if numRows >= 2:
            res.append([1,1])
            
            
        
        for i in range(3, numRows+1):
            output = [1] + [0] * (i - 2) + [1]
            for z in range(i-2):
                output[z+1] = res[-1][z] + res[-1][z+1]
            res.append(output)
        
        return res
        

        