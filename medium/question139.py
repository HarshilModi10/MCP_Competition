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
    
# using functional programming ot shorten the length of inner loop
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
            
            seg[i] = any( seg[j] and s[j:i] in wordDict for j in range(i))   
          
        return seg[-1]
    

#faster solution
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        cache = {}
        if not s:
            return True
        
        if not wordDict:
            return False

        word_dict = set(wordDict)
        return self.word_break(word_dict, s, 0, cache)
    
    def word_break(self, word_dict, s, index, cache):
        if not s:
            return True
        
        if index == len(s):
            return False
        
        if s[:index+1] in cache:
            return cache[s[:index+1]]
        
        if s[:index+1] in word_dict:
            temp = self.word_break(word_dict, s[index+1:], 0, cache) or self.word_break(word_dict, s, index+1, cache)
            cache[s[:index+1]] = temp
            return temp
        else:
            temp = self.word_break(word_dict, s, index+1, cache)
        
        cache[s[:index+1]] = temp
        return temp
        