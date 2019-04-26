class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver_1 = version1.split(".")
        ver_2 = version2.split(".")
        
        diff = len(ver_1) - len(ver_2)
        
        if diff > 0:
            ver_2 = ver_2 + [0] * diff
        else:
            ver_1 = ver_1 + [0] * -diff
        
        for i in range(len(ver_1)):
            if int(ver_1[i]) > int(ver_2[i]):
                return 1
            elif (int(ver_1[i])) < int(ver_2[i]):
                return -1
            else:
                continue
        
        return 0
            
                
        