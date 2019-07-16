class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = [0 for _ in range(26)]
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        
        for value in count:
            if value != 0:
                return False
            
        return True