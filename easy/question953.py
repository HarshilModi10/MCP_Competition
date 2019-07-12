class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic  = {}
        
        for i in range(len(order)):
            dic[order[i]] = chr(ord('a')+i)
        
        alpa = []
        
        for word in words:
            array = []
            for char in word:
                array.append(dic[char])
            alpa.append("".join(array))
        
        new_words = zip(words,alpa)
        
        new_words.sort(key=lambda x: x[1])
        
        for i in range(len(words)):
            if new_words[i][0] != words[i]:
                return False
            
        return True