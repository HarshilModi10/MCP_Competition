class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        #store the matched words
        match_list = []
        dic = {}
          
        
        #iterate over the dictionary
        for word in words:
            seen = set()
            for char in pattern:
                dic[char] = None
            match_list.append(word)
            if len(pattern) == len(word):          
                #check that the the permutations match
                for i in range(len(pattern)):
                    if dic[pattern[i]] is None and word[i] not in seen:
                        seen.add(word[i])
                        dic[pattern[i]] = word[i]
                    else:
                        if dic[pattern[i]] == word[i]:
                            continue
                        else:
                            match_list.pop()
                            break
        return match_list
                        
            
        