class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        words = sorted(words, key = lambda word: len(word))
        dic = {}
        for word in words:
            dic[word] = 1
        
        longest = 1
        for word in words:
            for i in range(len(word)):
                if word[:i] + word[i+1:] in dic:
                        dic[word] = max(dic[word], dic[word[:i] + word[i+1:]] + 1)
                        longest = max(longest,dic[word])
            
        return longest