class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dict or not sentence:
            return sentence
        
        dic = set(dict)
        words = sentence.split(" ")
        
        for i, word in enumerate(words):
            for j in range(1,len(word)+1):
                if word[:j] in dic:
                    words[i] = word[:j]
                    break
                
        return " ".join(words)
            
            
        
        