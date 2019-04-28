class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        self.stack = []
        
        for i,j in prerequisites:
            graph[i].append(j)
        
        for i in range(numCourses):
            if self.dfs(graph, visited, i):
                return []
        return self.stack
        
    
    def dfs(self,graph, visited, vertex):
        
        if visited[vertex] == -1:
            return True
        if visited[vertex] == 1:
            return False
        visited[vertex] = -1
        
        for pre in (graph[vertex]):
            if self.dfs(graph, visited, pre):
                return True
        self.stack.append(vertex)
        visited[vertex] = 1