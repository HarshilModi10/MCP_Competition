
# time O(N) * integer size and space: O(N) array
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


#Faster solution using dynamic programming space O(N) time O(N)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
        how does number of 1s work
        0 -> 0
        1 -> 1
        2 -> 10:1
        3 -> 11:2
        4 -> 100:1
        5 -> 101:2
        6: -> 110: 2
        7: -> 111: 3
        
        
        100100 -> 100011
        
        """
        if num == 0:
            return [0]
        
        bit = 1
        n_bit = bit << 1
        output = [0]
        
        for i in range(1,num+1):
            if n_bit <= i:
                bit = n_bit
                n_bit *= 2
                
            count = 1
            rem = i % bit
            count += output[rem]
            output.append(count)
            
        return output
            
            
        