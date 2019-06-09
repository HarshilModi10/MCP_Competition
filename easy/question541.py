class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ""
    
        string = list(s)
        
        slow = 0
        fast = k-1
        
        while slow < len(s):
            if fast < len(s):
                string = self.reverse(string, slow, fast)
            else:
                string = self.reverse(string, slow, len(s)-1)
            
            slow += 2*k
            fast += 2*k
        
        return "".join(string)
    
    
    def reverse(self, string, i, j):
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        
        return string
        