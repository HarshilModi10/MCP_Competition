class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        
        if not s:
            return 0
        
        return self.num_decodings(s, cache)

    
    def num_decodings(self, s, cache):
        
        
        if not s:
            return 1
        
        if s[0] == '0':
            return 0
        
        if s in cache:
            return cache[s]
        
        if len(s) >= 2 and int(s[:2]) <=26:
            cache[s] = self.num_decodings(s[1:], cache) + self.num_decodings(s[2:], cache)
        else:
            cache[s] = self.num_decodings(s[1:], cache)
        
        return cache[s]