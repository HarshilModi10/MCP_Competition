# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack = []
        stack.append(root)
        summation = set()
        
        while stack:
            node = stack.pop()
            if node.val in summation:
                return True
            summation.add(k - node.val)
            if node.right:
                stack.append(node.right)            
            if node.left:
                stack.append(node.left)
        
        return False