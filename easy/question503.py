class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        
        fib = [0] * (N)
        fib[0] = 0
        fib[1] = 1
        
        for i in range(2, N):
            fib[i] = fib[i-1] + fib[i-2]
        
        return fib[-1] + fib[-2]
        