class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        while num:
            if num == 1:
                return True
            if num % 4 == 0:
                num /= 4
            else:
                return False
        
        