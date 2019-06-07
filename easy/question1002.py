class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        dic1 = collections.defaultdict(int)
        dic2 = collections.defaultdict(int)
        output = []
        
        first_word = A[0]
        A = A[1:]
        
        for char in first_word:
            dic1[char] += 1
        
        for word in A:
            for char in word:
                if dic1[char] > 0:
                    dic2[char] += 1
                    dic1[char] -= 1
            dic1 = dic2
            dic2 = collections.defaultdict(int)
        

        for letter, count in dic1.items():
            for _ in range(count):
                output.append(letter)
        return output
            
            
            
                
        