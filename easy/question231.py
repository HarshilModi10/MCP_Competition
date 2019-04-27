class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        
        for i in range(33):
            if ((1<<i) & n):
                count +=1
        
        return count == 1
        