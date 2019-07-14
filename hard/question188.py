class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k = min(k,len(prices)//2)
        
        even_profits = [0 for i in range(len(prices))]
        odd_profits = [0 for i in range(len(prices))]
        
        for i in range(1,k+1):
            memo = [-float("inf")] * len(prices)
            if i%2 == 0:
                current_profits = even_profits
                previous_profits = odd_profits
            else:
                current_profits = odd_profits
                previous_profits = even_profits
            for j in range(1,len(prices)):
                memo[j] = max(memo[j-1], -prices[j-1] + previous_profits[j-1])
                current_profits[j] = max(current_profits[j-1], memo[j] + prices[j])

        return max(even_profits[-1], odd_profits[-1])
        
        