class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        global_max = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i] + nums[i-1], nums[i])
            global_max = max(global_max, nums[i])
        
        
        return global_max
        
#Faster solution

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max, global_max = -float("inf"), -float("inf")
        
        for num in nums:
            local_max = max(local_max + num, num)
            global_max = max(global_max, local_max)
        
        return global_max
        