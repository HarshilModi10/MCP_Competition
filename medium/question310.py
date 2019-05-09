class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        #create a map (vertex as key and edges as values)
        map = {k:set() for k in range(n)}
        
        #add the edges to the map
        for x,y in edges:
            map[x].add(y)
            map[y].add(x)
        
        #find all vertex with degree 1
        leaves = [k for k in map.keys() if len(map[k]) == 1]
        
        while n > 2:
            
            n -= len(leaves)
            #remove each leaf interatively
            
            new_leaves = []
            for leaf in leaves:
                next_leave = map[leaf].pop()
                map[next_leave].remove(leaf)
                if len(map[next_leave]) == 1:
                    new_leaves.append(next_leave)
                    
            leaves = new_leaves
            
        return leaves
                    
                