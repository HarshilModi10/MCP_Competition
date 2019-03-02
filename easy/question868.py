class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        globalMax = 0
        last = None
        
        for i in xrange(32):
            if (N >> i) & 1:
                if last is not None:
                    globalMax = max(globalMax, i - last)                    
                last = i
        return globalMax
        