class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        count = collections.Counter(s)
        
        string  = list(s)
        string.sort(key = lambda x: (count[x], x), reverse = True)
        
        return "".join(string)
        