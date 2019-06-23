class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[i], dp[i-1])
        
        
#faster solution

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = cost[0]
        f2 = cost[1]
        
        for i in range(2,len(cost)):
            f2, f1 = min(f1,f2) + cost[i], f2
        
        return min(f2,f1)
        
        