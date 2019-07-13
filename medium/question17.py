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
        
        res = []
        number = {"2": ["a", "b", "c"], 
                  "3": ["d", "e", "f"], 
                  "4": ["g","h", "i"], 
                  "5": ["j", "k", "l"], 
                  "6": ["m", "n", "o"], 
                  "7": ["p", "q", "r"], 
                  "8": ["s", "t", "u"], 
                  "9": ["v", "w", "x", "z"] }

        
        def get_combination(seq, digit):
            
            if not digit:
                res.append(seq)
            else:
                for letter in number[digit[0]]:
                    get_combination(seq+letter,digit[1:])
        
        
        if digits:
            get_combination("", digits)
        return res
                

  class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        key_pad = {2:['a','b','c'],
                   3:['d','e','f'],
                   4:['g','h','i'],
                   5:['j','k','l'],
                   6:['m','n','o'],
                   7:['p','q','r', 's'],
                   8:['t','u','v'],
                   9:['w','x','y','z']
                  }
        res = []
        
        self.letter_combo(key_pad, res, digits, [])
        return res
    
    def letter_combo(self, key_pad, res, digits, partial):
        if not digits:
            res.append("".join(partial))
            return 
        
        for letter in key_pad[int(digits[0])]:
            self.letter_combo(key_pad, res, digits[1:], partial + [letter])
            
            
        
        
        
        
                
        
        
            
            
        

        
        
        