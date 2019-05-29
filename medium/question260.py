class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        target = 0
        
        for num in nums:
            target ^= num
        
        index = 0
        
        #get the index where the bits is 1
        while (target & 1 == 0):
            target >>= 1
            index += 1
        
        temp = 1 << index
        
        num1 = 0
        num2 = 0
        
        for num in nums:
            if num & temp:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
        
        