class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        stack = []
        
        for s in S:
            if not stack:
                stack.append(s)
            elif stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        
        return "".join(stack)