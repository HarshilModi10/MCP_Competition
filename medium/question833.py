class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if not indexes:
            return S
        
        output = []
        read = 0
        current = 0
        
        replace = zip(indexes, sources, targets)
        replace.sort()
        
        while read < len(S):
            if current < len(indexes) and read == replace[current][0]:
                if S[read:read + len(replace[current][1])] == replace[current][1]:
                    output.append(replace[current][2])
                    read += len(replace[current][1])
                else:
                    output.append(S[read])
                    read += 1
                
                current += 1
            
            else:
                output.append(S[read])
                read += 1
        
        return "".join(output)