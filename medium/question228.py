class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        res = []
        start = 0
        
        if not nums:
            return []
        
        for i in range(1,len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if i - start == 1:
                    res.append(str(nums[start]))
                    start = i
                else:
                    string = str(nums[start]) + "->" + str(nums[i-1])
                    res.append(string)
                    start = i
        
        
        if len(nums) - start == 1:
            res.append(str(nums[-1]))
        else:
            string = str(nums[start]) + "->" + str(nums[-1])
            res.append(string)
        
        return res
            
        