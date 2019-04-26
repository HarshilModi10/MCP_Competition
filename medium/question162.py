class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums) -1    
        
        #binary search for peak
        while (l < r):            
            mid = (l + r)/2            
            if (nums[mid] < nums[mid+1]):
                l = mid + 1
            else:
                r = mid
                
        return l
            
        