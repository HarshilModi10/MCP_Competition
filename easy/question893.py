class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        unique = set()
        
        for word in A:
            characters = [0] * 52
            for i in range(len(word)):
                if i%2 == 0:
                    characters[ord(word[i]) - ord("a")] += 1
                else:
                    characters[ord(word[i]) - ord("a") + 26] += 1
            
            unique.add(tuple(characters))
        
        return len(unique)
                
        