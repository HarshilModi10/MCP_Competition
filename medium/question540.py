class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_pointer, right_pointer = 0, len(nums) - 1
        
        while left_pointer < right_pointer:
            mid = left_pointer/2 + right_pointer/2
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left_pointer = mid+1
                else:
                    right_pointer = mid
            else:
                if nums[mid] == nums[mid-1]:
                    left_pointer = mid+1
                else:
                    right_pointer = mid
                    
        return nums[left_pointer]