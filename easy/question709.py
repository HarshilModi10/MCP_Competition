class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        output = []
        for i in range(len(str)):
            if 65<=ord(str[i]) <= 90:
                output.append(chr(ord(str[i]) + 32))
            else:
                output.append(str[i])
        
        return "".join(output)