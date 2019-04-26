class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        
        
        def combination(com, can, target):
            
            if target == 0:
                res.append(com)
            
            elif target > 0 and can:
                combination(com+[can[0]], can, target - can[0])
                combination(com, can[1:], target)
            
        
        
        combination([], candidates, target)
        return res