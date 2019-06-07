class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        globalMax = 0
        start = 0
        end = len(height)-1
        
        while start < end:
            localMax = min(height[start], height[end]) * (end-start)
            
            if localMax > globalMax:
                globalMax = localMax
            
            if height[start] < height[end]:
                start +=1
            else:
                end -= 1
                
        return globalMax

#another solution 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        volume = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            volume = max(volume, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return volume
        
        