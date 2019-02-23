class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n, sorts = len(nums), sorted(nums)
        if nums == sorts: return 0
        l, r = min(i for i in range(n) if nums[i] != sorts[i]), max(i for i in range(n) if nums[i] != sorts[i])
        return r - l + 1
        