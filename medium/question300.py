class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        globalMax = 1
        
        for i in range(len(nums)):
            localMax = dp[i]
            
            for j in range(i):
                if nums[i] > nums[j]:
                    localMax = max(dp[j]+1, localMax)
            
            dp[i] = localMax
            if localMax > globalMax:
                globalMax = localMax
        

        return globalMax
    
     