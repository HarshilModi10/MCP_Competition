class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums[abs(num)-1] < 0:
                return abs(num)
            else:
                nums[abs(num)-1] *= -1
        