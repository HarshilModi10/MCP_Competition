class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        write_index = 0
        
        for num in nums:
            if num != 0:
                nums[write_index] = num
                write_index += 1
        
        while write_index < len(nums):
            nums[write_index] = 0
            write_index += 1
        
                
        