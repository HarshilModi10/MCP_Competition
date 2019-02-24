class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for i in range(k):
            
            nums[:] = nums[-1:] + nums[:length -1]
        
        
        
        
        