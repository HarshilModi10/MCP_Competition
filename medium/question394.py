class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack= []
        count = 0
        string = ""
        
        for c in s:
            if c == '[':
                stack.append(string)
                stack.append(count)
                count = 0
                string = ""
            
            elif c == ']':
                num = stack.pop()
                current = stack.pop()
                string = current + num*string
            
            elif c.isdigit():
                count = count*10 + int(c)
            else:
                string += c
        
        return string
        