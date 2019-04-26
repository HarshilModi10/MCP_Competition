class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        seg = [False] * len(s) + [False]
        seg[0] = True
        
        for i in range(1,len(s)+1):
            for j in range(i):
                if seg[j] and s[j:i] in wordDict:
                    seg[i] = True
                    break        
          
        return seg[-1]
    
