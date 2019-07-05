class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.count_solutions(nums, S, 0, 0)
    
    def count_solutions(self, nums, S, index, total):
        if index == len(nums):
            if total == S:
                return 1
            return 0
        else:
            return self.count_solutions(nums, S, index + 1, total + nums[index]) + self.count_solutions(nums, S, index +1, total - nums[index])
        
        