class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        res = []
    
        
        for num in nums:
            if num in dic:
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1
        
        res = sorted(dic, key = dic.get,reverse = True)
        return(res[:k])
        

        
        
        