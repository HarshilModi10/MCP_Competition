"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        dept = 0
        for child in root.children:
            height = self.maxDepth(child)
            dept = max(dept, height)
        
        return dept + 1
        