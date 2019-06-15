"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = []
        preorder = []
        stack.append(root)
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            
            for i in range(len(node.children)-1, -1, -1):
                stack.append(node.children[i])
        
        return preorder
        