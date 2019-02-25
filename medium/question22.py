class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        
        return self.generate("", n, 0)
        
    def generate(self, cur, openP, closeP):
        
        if openP == 0:
            return [cur + ")" * closeP]
        if closeP == 0:
            return self.generate(cur + "(", openP - 1, 1)
        else:
            return self.generate(cur + '(', openP - 1, closeP + 1) + self.generate(cur + ')', openP, closeP - 1)
        
        