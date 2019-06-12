class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #initialize variables
        total_max = 0
        local_max = 0
        
        for digit in nums:
            if digit == 1:
                local_max += 1
            else:
                total_max = max(total_max, local_max)
                local_max = 0
        total_max = max(local_max, total_max)
        return total_max
        
        