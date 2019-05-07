class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        
        indexS = 0
        indexT = 0
        
        while indexT <len(t):
            if indexS == len(s):
                return True
            if s[indexS] == t[indexT]:
                indexS += 1
            indexT += 1
        
        return len(s) == indexS
        
        
        
        