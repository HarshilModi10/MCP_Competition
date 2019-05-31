#constant space and linear time
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        total = 0
        for i in range(len(s)):
            total ^= ord(s[i])
            total ^= ord(t[i])
        
        total ^= ord(t[-1])
        
        return chr(total)
        