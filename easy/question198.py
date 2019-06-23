class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        f1, f2 = 0, 0
        
        for i in range(len(nums)):
            f2,f1 = max(f2, f1 + nums[i]), f2
            
        return f2
        
        