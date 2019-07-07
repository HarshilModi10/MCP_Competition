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
            

#slower solution 

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not amount:
            return 1
        if not coins:
            return 0
        
        dp = [[0] * (amount+1) for _ in range(len(coins))] 
    
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for j in range(len(coins)):
            for i in range(1,amount+1):
                if coins[j] <= i:
                    dp[j][i] += dp[j][i-coins[j]]
                if j != 0:
                    dp[j][i] += dp[j-1][i]
        return dp[-1][-1]


#another approach

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0] * (amount+1) for i in range(len(coins)+1)]
        
        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= amount:
                    dp[i][j] += dp[i][j - coins[i-1]]
                dp[i][j] += dp[i-1][j]
                
        return dp[-1][-1]