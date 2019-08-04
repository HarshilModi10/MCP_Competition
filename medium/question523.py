class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #check for zero case
        if k < 0:
            k = k * -1
        
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] == 0:
                    return True
            return False
        
        #initialize variables 
        remainder = {0:-1}
        summation = 0
        
        #iterate through the array and count total sums
        for i, num in enumerate(nums):
            summation += (num)
            summation = summation % k
            #check if k - reminder is in remainders list
            if summation in remainder and (i - remainder[summation]) >= 2:
                return True
            #add the reminder sum plus end index to the reminder variable
            if summation not in remainder:
                remainder[summation] = i
        
        return False
            
    