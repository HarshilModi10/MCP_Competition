class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        intersection = collections.defaultdict(int)
        output = []
        
        #add the count of numbers from list 1
        for num in nums1:
            intersection[num] += 1
        
        # add same letters to output array
        for num in nums2:
            if num in intersection and intersection[num] > 0:
                output.append(num)
                intersection[num] -= 1
        
        return output
            
            
        