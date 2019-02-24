class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        res = []
        
        for i in range(left,right+1):
            istrue = True
            for j in (str(i)):

                if int(j) == 0 or i % int(j) != 0:
                    istrue = False
                    break
            if istrue:
                res.append(i)
        
        return res
                    
                
        