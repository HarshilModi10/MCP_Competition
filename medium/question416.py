class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True 
        total = sum(nums)
        if total %2 != 0:
            return False
        
        return self.helper(nums, total/2, 0, collections.defaultdict(dict))
    
    def helper(self, nums, total, index, cache):
        
        if total == 0:
            return True 
        if index >= len(nums):
            return False
        
        if total in cache[index]:
            return cache[index][total]
        
        else:
            cache[index][total] = self.helper(nums, total, index+1, cache)
            if total >= nums[index]:
                cache[index][total] = cache[index][total] or self.helper(nums, total-nums[index], index+1, cache)
        return cache[index][total]
        
        
        
        