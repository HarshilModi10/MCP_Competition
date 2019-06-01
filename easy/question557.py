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
        