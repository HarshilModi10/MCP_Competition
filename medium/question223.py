class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        t_y = min(H,D)
        t_x = max(A,E)
        
        b_x = min(C, G)
        b_y = max(F, B)
        
        total_common = (b_x - t_x) * (t_y - b_y)
        if total_common < 0 or (b_x - t_x) < 0 or (t_y - b_y) < 0:
            total_common = 0
        
        return (C - A) * (D - B) + (H - F) * (G - E) - total_common