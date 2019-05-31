
# time O(N) * integer size and space: O(N)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        output = []
        
        for i in range(num+1):
            output.append(self.count_number(i))
        
        #return the output array
        return output
    
    def count_number(self, num):
        #array to keep tract of count
        count = 0
        
        #count the number of 1s 
        while num:
            if num & 1:
                count += 1                
            num >>= 1
        
        return count