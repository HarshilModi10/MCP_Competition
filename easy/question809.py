class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        #initialize variables
        total_lines = 1
        current_width = 0
        
        for char in S:
            current_width += widths[ord(char) - ord("a")]
            if current_width > 100:
                total_lines += 1
                current_width = widths[ord(char) - ord("a")]
                
        return [total_lines, current_width]
        