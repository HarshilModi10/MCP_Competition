class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #create a counter to count palindromes
        count = 0
        
        #iterate over the string
        for i in range(len(s)):
            count += self.count_palandrome(s, i,i)
            if i != len(s)- 1 and s[i] == s[i+1]:
                count += self.count_palandrome(s, i,i+1)
        
        return count
    
    def count_palandrome(self, s,l, r):
        
        if 0 > l or r >= len(s) or s[l] != s[r]:
            return 0
        else:
            return self.count_palandrome(s, l-1, r+1) + 1
        