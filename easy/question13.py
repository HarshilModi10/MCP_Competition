class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_symbols = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        special_symbols = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        total = 0
        index = 0
        
        while index < len(s):
            if index != len(s) - 1 and s[index:index+2] in special_symbols:
                total += special_symbols[s[index:index+2]]
                index += 2
            else:
                total += roman_symbols[s[index]]
                index += 1
        
        return total