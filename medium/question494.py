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
        

#memoization solution

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        cache = {}
        return self.count_solutions(nums, S, 0, 0, cache)
    
    def count_solutions(self, nums, S, index, total, cache):
        if (index, total) in cache:
            return cache[(index, total)]
        else:
            if index == len(nums):
                if total == S:
                    return 1
                return 0
            else:
                cache[(index, total)] = self.count_solutions(nums, S, index + 1, total + nums[index], cache) + self.count_solutions(nums, S, index +1, total - nums[index], cache)
                return cache[(index, total)]
        
#dynamic programming solution

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        cache = {0:1}
        
        for num in nums:
            new = collections.defaultdict(int)
            for key, value in cache.items():
                new[key+num] += value
                new[key-num] += value
            cache = new
        
        return cache[S]
    
        
        
        

