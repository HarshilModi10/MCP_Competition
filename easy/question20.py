class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []        
        dic = {"(": ")", 
               "[": "]", 
               "{": "}" }
        
        for char in s:
            if char in dic:
                stack.append(dic[char])
            elif stack and stack[-1] == char:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        
        return False
                