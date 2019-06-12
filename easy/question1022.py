# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        #get sum of path
        return self.sum_path(root, "")
            
    def sum_path(self, root, binary):
        
        if not root.right and not root.left:
            binary += str(root.val)
            return int(binary, 2)
        elif not root.right:
            return self.sum_path(root.left, binary + str(root.val))
        elif not root.left:
            return self.sum_path(root.right, binary + str(root.val))
        else:
            left = self.sum_path(root.left, binary + str(root.val))
            right = self.sum_path(root.right, binary + str(root.val))
            return left + right
        
        