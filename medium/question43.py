class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total = 0
        place = 1
        
        for i in range(len(num2) -1, -1, -1):
            total += int(num1) * int(num2[i]) * place
            place *= 10
        
        return str(total)
        