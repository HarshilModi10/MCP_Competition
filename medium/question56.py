# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start)
        res = []
        
        for num in intervals:
            if not res or res[-1].end < num.start:
                res.append(num)
            else:
                res[-1].end = max(num.end, res[-1].end)
        return res
        
        
        
        
        