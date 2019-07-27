class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        bijection = {}
        seen = set()
        seen_words = set()
        sentence = str.split(" ")
        
        if len(pattern) != len(sentence):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in bijection:
                if bijection[pattern[i]] != sentence[i]:
                    return False
            else:
                if pattern[i] in seen or sentence[i] in seen_words:
                    return False
                else:
                    bijection[pattern[i]] = sentence[i]
                    seen.add(pattern[i])
                    seen_words.add(sentence[i])
        return True
            
        
        