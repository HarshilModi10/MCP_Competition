# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.max_path = -float("inf")
        self.max_path_sum(root)
        return self.max_path
        
    def max_path_sum(self, root):
        
        if not root:
            return 0
        
        L = max(0, self.max_path_sum(root.left))
        R = max(0, self.max_path_sum(root.right))
        
        self.max_path = max(self.max_path, L+R + root.val)
        
        return max(R, L) + root.val