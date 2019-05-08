class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse = True)
        
        for i, num in enumerate(citations):
            if i+1 >= num:
                return i+1 if num == i+1 else i
        
        return len(citations)
        