class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s) - 1
        column_number = 0
        
        for char in s:
            column_number += (ord(char) - ord('A') + 1) * (26 ** size)
            size -= 1
        
        return column_number