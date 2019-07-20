class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split(" ")
        output = []
        
        for word in words:
            output.append(word[::-1])
        
        return " ".join(output)
        

# faster solution

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        words = s.split(" ")
        
        for i, word in enumerate(words):
            words[i] = word[::-1]
        
        return " ".join(words)
    
            