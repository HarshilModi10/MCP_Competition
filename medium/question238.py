class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        for i in range(len(nums)-1):
            output[i+1] *= nums[i] * output[i]
        total = 1  
        for i in range(len(nums)-1,0,-1):
            total *= nums[i]
            output[i-1] *= total
        
        return output
            