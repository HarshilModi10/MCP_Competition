class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 31
        while (num >> n) & 1 != 1:
            n -= 1   

        for i in range(n + 1):
            num = num ^ (1 << i)

        return num