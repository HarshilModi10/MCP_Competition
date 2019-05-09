class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        val = 0
        set_list = [set(word) for word in words]
        
            
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not (set_list[i] & set_list[j]):
                    val = max(val, len(words[i])*len(words[j]))
        return val