class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        self.longest = ""
        
        #iterate over input string and check is palindrome
        for i in range(len(s)):
            self.longest_palindrome(s,i,i)
            if i+1 < len(s) and s[i] == s[i+1]:
                self.longest_palindrome(s,i,i+1)
    
        return self.longest
    
    #get the longet palindrome
    def longest_palindrome(self, s,l, r):
        #update longest
        if len(self.longest) < r-l+1:
            self.longest = s[l:r+1]
        
        if 0 <= l - 1 and r+1 < len(s) and s[l-1] == s[r+1]:
            self.longest_palindrome(s,l-1,r+1)
            
        
        
            
        
        