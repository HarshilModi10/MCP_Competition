class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        unique = set()
        
        for num in A:
            if num in unique:
                return num
            unique.add(num)