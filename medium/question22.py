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

# different solution

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def generate(string, n,openP):
            
            if n == 0:
                res.append(string + ")"* openP)
            elif openP == 0:
                generate(string + "(", n-1, 1)
            else:
                generate(string + "(", n -1, openP + 1)
                generate(string + ")", n, openP-1)  
        
        
        
        
        res = []
        generate("", n,0)
        return res

    # quicker solution

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []        
        
        def generate(seq, n,num_open):            
            if n == 0 and num_open == 0:
                res.append(seq)            
            elif n == 0:
                generate(seq+")", n, num_open - 1)
            
            elif num_open == 0:
                generate(seq+"(", n-1, num_open + 1)
            else:
                generate(seq+")", n, num_open - 1)
                generate(seq+"(", n -1, num_open + 1)
        
        if n:
            generate("", n, 0)
        
        return res
        
        
        
        