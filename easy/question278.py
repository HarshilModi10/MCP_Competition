# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_pointer, right_pointer = 1, n
        
        while left_pointer < right_pointer:
            mid = left_pointer + (right_pointer - left_pointer)/2
            if isBadVersion(mid):
                right_pointer = mid
            else:
                left_pointer = mid + 1
        
        return left_pointer
        