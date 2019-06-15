class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram:
                anagram_list = anagram[sorted_word]
                anagram_list.append(word)
                anagram[sorted_word] = anagram_list
            else:
                anagram[sorted_word] = [word]
        
        return [group for group in anagram.values()]
                    