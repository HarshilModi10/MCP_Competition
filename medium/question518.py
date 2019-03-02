class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        res = [1] + [0] * amount
        
        for coin in coins:
            for i in range(amount+1):
                if i >= coin:
                    res[i] = res[i] + res[i - coin]
                    
        return res[amount]
            
        