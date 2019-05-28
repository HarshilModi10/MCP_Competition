# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        return self.helper_path_sum(root, sum)
    
    def helper_path_sum(self, node, sum):
        
        if not node:
            return False
        
        if not node.left and not node.right:
            return sum == node.val

        
        else:
            return self.helper_path_sum(node.left, sum - node.val) or self.helper_path_sum(node.right, sum - node.val)
        return False
        
#faster solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if not root:
            return False 
        
        if not root.right and not root.left and root.val == sum:
            return True 
        
        return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)