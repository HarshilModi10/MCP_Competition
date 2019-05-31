class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        #create a hashset of sequences and fequency
        sequence_count = {}
        output_array = []
        left_pointer = 0
        right_pointer = 10
        
        #iterate over string and compute substrings
        while right_pointer <= len(s):
            string  = s[left_pointer:right_pointer]
            
            #check if string is already in sequence and count is one
            if string in sequence_count:
                if sequence_count[string] == 1:
                    output_array.append(string)
                    sequence_count[string] += 1
            #else at it to the hashset
            else:
                sequence_count[string] = 1
            left_pointer += 1
            right_pointer += 1
        
        return output_array
            