class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        heap = []
        heapq.heappush(heap,(matrix[0][0], 0, 0))
        
        while heap:
            element, m, n = heapq.heappop(heap)
            k -= 1
            if k == 0:
                return element
            
            if n + 1 != len(matrix) and (matrix[n+1][m], m, n+1) not in heap:
                heapq.heappush(heap, (matrix[n+1][m], m, n+1))
            if m+1 != len(matrix[0]) and (matrix[n][m+1], m+1, n) not in heap:
                heapq.heappush(heap, (matrix[n][m+1], m+1, n))

            

                
                
                             
        