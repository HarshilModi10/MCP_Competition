# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        Node_val = self.count_path_sum(root, limit, 0)
        if Node_val:
            return None
        return root
    
    def count_path_sum(self, root, limit, total):
        if not root:
            return total < limit

        if root.left and root.right:
            L = self.count_path_sum(root.left, limit, total + root.val)
            R = self.count_path_sum(root.right, limit, total + root.val)
        elif root.left and not root.right:
            L = self.count_path_sum(root.left, limit, total + root.val)
            R = True
        elif root.right and not root.left:
            L = True
            R = self.count_path_sum(root.right, limit, total + root.val)
        else:
            return total + root.val < limit
        
        if L and R:
            return True 
        if L:
            root.left = None
        if R:
            root.right = None
            
        return False