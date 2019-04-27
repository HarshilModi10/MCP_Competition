class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #create a graph and a visited list
        graph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        
        #add prerequisites
        for i,j in prerequisites:
            graph[i].append(j)
        
        for i in range(numCourses):
            if self.dfs(graph,visited,i):
                return False
        return True
    
    #preform bfs on the vertex to find a cycle
    def dfs(self, graph, visited, vertex):
        
        if visited[vertex] == -1:
            return True
        if visited[vertex] == 1:
            return False
        
        visited[vertex] = -1
        for pre in  graph[vertex]:
            if self.dfs(graph, visited, pre):
                return True
        visited[vertex] = 1
        return False
            