# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        #list to hold the paths
        self.paths = []
        
        self.helperPathSum(root, sum, [])
        return self.paths
    
    #helper function to get path of root to leaf
    def helperPathSum(self, root,sum, path):
        
        if not root:
            return None
        
        if root.val == sum and not root.left and not root.right:
            self.paths.append(path + [root.val])
        
        self.helperPathSum(root.left, sum - root.val, path + [root.val]) 
        self.helperPathSum(root.right, sum - root.val, path + [root.val])
        
        