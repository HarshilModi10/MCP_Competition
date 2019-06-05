class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        #initialize variables
        min_price = prices[0]
        max_price = prices[0]
        max_sum = 0
        
        for num in prices:
            if num < min_price:
                max_sum = max(max_sum, max_price - min_price)
                min_price = num
                max_price = num
            elif num > max_price:
                max_price = num
        
        return max(max_sum, max_price - min_price)
        