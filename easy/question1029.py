class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda costs: abs(costs[0] - costs[1]))
        city_A = len(costs)/2
        city_B = len(costs)/2
        total = 0
        
        for i in range(len(costs)-1,-1,-1):
            if costs[i][0] < costs[i][1]:
                if city_A > 0:
                    total += costs[i][0]
                    city_A -= 1
                else:
                    total += costs[i][1]
                    city_B -= 1
            else:
                if city_B > 0:
                    total += costs[i][1]
                    city_B -= 1
                else:
                    total += costs[i][0]
                    city_A -= 1
        return total
                
            