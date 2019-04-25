class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carry = 0
        
        for i in range(len(digits)-1, -1,-1):
            if digits[i] == 9:
                digits[i], carry = 0, 1
            else:
                digits[i] += 1
                carry = 0
                break
        
        if carry:
            return [1] + digits
        
        return digits
                
        