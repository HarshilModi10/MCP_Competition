class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b:
            return ""
        a = list(a)
        b = list(b)
        carry = 0
        output = []
        
        while a or b:
            total = carry
            if a:
                total += int(a.pop())
            if b:
                total += int(b.pop())
                
            carry = total/2
            output.append(str(total%2))
        
        if carry:
            output.append("1")
        
        return "".join(output[::-1])
            
        