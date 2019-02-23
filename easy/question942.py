class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low, high = 0, len(S)
        res = []
        
        for i in S:
            if i == "I":
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        
        return res + [low]
                
        