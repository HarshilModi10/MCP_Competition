"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return None
        
        def clone(node, dict):
            if node not in dict:
                dict[node] = Node(node.val, [])
                for n in node.neighbors:
                    dict[node].neighbors.append(clone(n, dict))
            return dict[node]
        
        return clone(node, {})
