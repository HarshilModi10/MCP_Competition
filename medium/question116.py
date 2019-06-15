"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        # is not root then return
        if not root:
            return None
        
        queue = []
        queue.append(root)
        
        while queue:
            
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
                
            queue[-1].next = None
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return root
                
            
        