# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        
        while l < r:
            gues = l + (r-l)/2
            result = guess(gues)
            if result == 0:
                return gues
            elif result == -1:
                r = gues - 1
            else:
                l = gues + 1
        
        return l
        
        