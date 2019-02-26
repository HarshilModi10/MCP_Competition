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
        