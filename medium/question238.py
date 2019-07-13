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

# Faster solution

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        
        for i in range(1,len(nums)):
            output[i] *= output[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1, -1):
            output[i] *= nums[i+1]
            nums[i] *= nums[i+1]
        
        return output
            