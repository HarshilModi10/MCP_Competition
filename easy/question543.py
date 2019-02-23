# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.diameter(root)
        return self.max - 1
    
    def diameter(self,root):
        if not root:
            return 0
        
        L = self.diameter(root.left)
        R = self.diameter(root.right)
        
        self.max = max(self.max,L+R+1)
        return max(L,R) + 1
        