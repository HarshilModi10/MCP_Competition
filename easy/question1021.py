class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        output = ""
        count = 0
        stack = []
        
        for s in S:
            if s == "(":
                stack.append(s)
                count += 1
            elif s == ")" and count == 1:
                output += "".join(stack[1:])
                count = 0
                stack = []
            else:
                stack.append(s)
                count -= 1
        
        return output
                
            
                
        