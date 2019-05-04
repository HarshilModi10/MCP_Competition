class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        if not nums:
            return []
        
        self.backtracking(nums, res,[],0)
        return res
    
    def backtracking(self,nums, res,subset,index):
        res.append(subset)        
        for i in range(index,len(nums)):
            if index < i and nums[i] == nums[i-1]:
                continue
            self.backtracking(nums,res,subset + [nums[i]],i+1)
    