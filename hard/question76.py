class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashMap = {}
        
        if len(s) < len(t):
            return ""
        
        for c in t:
            if c in hashMap:
                hashMap[c] = hashMap[c] + 1
            else:
                hashMap[c] = 1

        min_length = len(s) + 2
        index = 0;
        slow = fast = 0
        
        while (slow <len(s)):
            
            # if window is valid move slow pointer
            while self.valid_window(hashMap):
                
                if min_length > fast - slow:
                    min_length = fast - slow
                    index = slow
                if s[slow] in hashMap:                    
                    hashMap[s[slow]] += 1
                slow += 1
            
            #else move the faster pointer
            else:              
                
                if fast < len(s) and s[fast] in hashMap:                                     
                    hashMap[s[fast]] -= 1
                
                #test to check if end has been reached
                elif fast >= len(s):
                    break
                fast += 1
        
        if min_length <= len(s):
            return s[index:index+min_length]
        return ""
    
    def valid_window(self, hashMap):
        
        for num in hashMap.values():
            if num > 0:
                return False
        return True
            
                    
        