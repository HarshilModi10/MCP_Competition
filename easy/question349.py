class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = set()
        output = []
        
        for num in nums1:
            nums.add(num)
        
        for num in nums2:
            if num in nums and num not in output:
                output.append(num)
        
        return output