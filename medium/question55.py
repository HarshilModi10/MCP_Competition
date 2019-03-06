class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxJump = 0
        
        for i in range(len(nums)-1):
            maxJump = max(maxJump-1, nums[i])
            
            if maxJump == 0:
                return False
        
        return True
        
        