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
            
            
# assume array is sorted

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1.sort()
        nums2.sort()
        index1 = 0
        index2 = 0
        output = []
        
        #while we are in a valid location
        while  index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                output.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                index1 += 1
        
        return output
            
            
            
        