# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0
        
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        self.bstToGst(root.right)
        self.total += root.val
        root.val = self.total
        self.bstToGst(root.left)
        return root
        