# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.valid(root, float('-inf'), float('inf'))
        
    def valid(self, root, low, high):
        if not root:
            return True
        if root.val < low or root.val > high:
            return False
        return self.valid(root.left, low, root.val - 1) and self.valid(root.right, root.val+1, high)
    