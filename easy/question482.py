class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = "".join(S.split("-"))
        res = []
        first_group = len(S)%K
        index = 0
        if first_group:
            res.append(S[index:first_group])
            index = first_group
        
        while index < len(S):
            res.append(S[index:index+K])
            index += K

        return '-'.join(res).upper()

        
            
            
            
        