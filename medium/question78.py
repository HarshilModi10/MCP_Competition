class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        self.dfs(res,nums, [],0)
        return res

    #backtracking implemented
    def dfs(self, res, nums, path, index):
        
        res.append(path)        
        for i in range (index, len(nums)):
            self.dfs(res,nums,path + [nums[i]], i + 1)
        
        
        