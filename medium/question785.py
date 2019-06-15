class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        visited = {}
        queue = []
        
        for i in range(len(graph)):
            if i not in visited:
                queue.append(i)
                visited[i] = 1
                
                while queue:
                    cur = queue.pop()
                    
                    for edge in graph[cur]:
                        if edge not in visited:
                            visited[edge] = visited[cur] * -1 
                            queue.append(edge)
                        elif visited[edge] == visited[cur]:
                            return False
        return True
                            
                    
                