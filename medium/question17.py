class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        return [a + b for a in map[digits[0]] for b in (self.letterCombinations(digits[1:]) or ['']) ] if digits else []

        
        
#backtracking
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def back_tracking(com, digit):
            if not digit:
                output.append(com)
            else:
                
                for letter in map[digit[0]]:
                    back_tracking(com+letter,digit[1:])
        
        
        
        output = []
        if digits:
            back_tracking("", digits)
            
        return output
        

        
        
        