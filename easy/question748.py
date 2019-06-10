class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        word_list = collections.defaultdict(int)
        diff = 0
        shortest = None
        #get a count of the words in the licensePlate
        for char in licensePlate:
            if char != " " and not char.isdigit():
                word_list[char.lower()] += 1
                diff += 1
        
        for word in words:
            local_word = word_list.copy()
            local_diff = diff
            for char in word:
                if char.lower() in local_word and local_word[char.lower()] > 0:
                    local_word[char.lower()] -= 1
                    local_diff -= 1
                    
            if local_diff == 0:
                if not shortest or len(word) < len(shortest):
                    shortest = word               
        
        return shortest
                
        
        