class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        output = []
        val = 0
        
        for x, y in points:
            distance = -1 * (x * x + y * y)
 
            heapq.heappush(heap,(distance, [x, y]))
            
            if len(heap) > K:

                heapq.heappop(heap)
        
        while heap:
            local, point = heapq.heappop(heap)
            output.append(point)
            

        return output
            
        