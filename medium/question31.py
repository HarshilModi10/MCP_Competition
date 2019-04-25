class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        swap = False
        
        def get_swap_index(i, swap_num):
            n = i
            for num in range(i, len(nums)):
                if nums[num] > swap_num and nums[num] <= nums[n]:
                    n = num          
            return n
        
        def reverse(i):
            start, end = i, len(nums)-1
            while end > start:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -= 1
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = get_swap_index(i, nums[i-1])
                nums[index],nums[i-1] = nums[i-1], nums[index]
                reverse(i)
                swap = True 
                break
                    
        if not swap and nums:
            reverse(0)   
        
        
        
            
            
        