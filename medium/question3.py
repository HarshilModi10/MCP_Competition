class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #create left and right pointer and hashmap of characters
        slow = 0
        fast = 0
        character = set()
        length = 0
        
        #loop over the string while right is less then length of S
        while (fast < len(s)):
            #if s at index fast is not in dic add it and move fast left
            #update length 
            if s[fast] not in character:
                character.add(s[fast])
                fast += 1
                length = max(length, fast - slow)            
            
            #else move slow right until s at index i is not in dic
            else:
                character.remove(s[slow])
                slow += 1
        
        return length
        