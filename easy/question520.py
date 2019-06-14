class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        count = 0
        capital = False
        #check if first letter is capitial

        if (ord(word[0]) - ord("A")) < 26:
            capital = True
        
        
        for i in range(1, len(word)):
            if ord(word[i]) - ord("A") < 26:
                count += 1
         

        if capital == True and count == len(word) - 1:
            return True
        
        if count == 0 :
            return True 
        return False

        