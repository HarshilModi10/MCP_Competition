class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False
        
        word_count = collections.defaultdict(int)
        for char in magazine:
                word_count[char] += 1
        
        for char in ransomNote:
            if word_count[char] > 0:
                word_count[char] -= 1
            else:
                return False
            
        return True 
            
        
        
        