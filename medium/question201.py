class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        shift = 0
        while n != m:
            n >>= 1
            m >>= 1
            shift += 1
            
        return n << shift