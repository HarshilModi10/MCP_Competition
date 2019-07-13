class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        
        #get the total sum of the array
        total = sum(nums)
        
        #variable to keep track of current sum
        relative_sum = 0
        
        #iterate over the array and check partial sum
        for i in range(len(nums)):
            if i != 0:
                relative_sum += nums[i-1]
                
            if relative_sum == total - relative_sum - nums[i]:
                return i
            
        return -1
        
 