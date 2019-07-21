class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or newColor == image[sr][sc]:
            return image
        
        self.flood_fill(image, sr, sc, newColor, image[sr][sc])
        return image
    
    def flood_fill(self, image, sr, sc, newColor, oldColor):
        
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != oldColor:
            return None
        
        image[sr][sc] = newColor
        
        return self.flood_fill(image, sr+1, sc, newColor, oldColor) or self.flood_fill(image, sr-1, sc, newColor, oldColor) or self.flood_fill(image, sr, sc+1, newColor, oldColor) or self.flood_fill(image, sr, sc-1, newColor, oldColor)