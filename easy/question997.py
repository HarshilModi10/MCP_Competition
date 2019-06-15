class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return 1
        #create a graph:
        indegree = collections.defaultdict(list)
        outdegree = collections.defaultdict(list)
        
        for person, trusts in trust:
            indegree[trusts].append(person)
            outdegree[person].append(trusts)
        
        for key, val in indegree.items():
            if len(val) == N - 1 and key not in outdegree:
                return key
        
        return -1
                
        