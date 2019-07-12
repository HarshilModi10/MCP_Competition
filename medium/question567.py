class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        if not s1:
            return True 
        
        permutation = collections.defaultdict(int)
        diff = 0
        
        for c in s1:
            permutation[c] += 1
            diff += 1
        
        left_pointer, right_pointer = 0, 0
        
        while right_pointer < len(s2):
            
            if left_pointer == right_pointer:
                if s2[left_pointer] not in permutation:
                    left_pointer += 1
                    right_pointer += 1
                else:
                    diff -= 1
                    permutation[s2[right_pointer]] -= 1
                    right_pointer += 1

            else:
                if s2[right_pointer] not in permutation:
                    permutation[s2[left_pointer]] += 1
                    left_pointer += 1
                    diff += 1
                    
                elif permutation[s2[right_pointer]] > 0:
                    diff -= 1
                    permutation[s2[right_pointer]] -= 1
                    right_pointer += 1
                else:
                    permutation[s2[left_pointer]] += 1
                    diff += 1
                    left_pointer += 1
                    
            if diff == 0:
                return True 
                    
        return False
                
                    