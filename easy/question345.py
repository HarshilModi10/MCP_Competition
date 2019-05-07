class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s)- 1
        vowel_set = ('a', 'e', 'i', 'o', 'u')
        
        while (start < end):
            if s[start].lower() not in vowel_set:
                start += 1
            elif s[end].lower() not in vowel_set:
                end -= 1                
            elif s[start].lower() in vowel_set and s[end].lower() in vowel_set:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        return ''.join(s)
            
                
            
        