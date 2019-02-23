class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        moorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique = set()
        
        for word in words:
            output = ""
            for i in range(len(word)):
                output = output + moorse[ord(word[i]) - 97]
            unique.add(output)
        
        return len(unique)
                
                
        