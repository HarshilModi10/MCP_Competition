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
    
#faster solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.max = 0
        self.getMax(root)
        return self.max
    
    def getMax(self, root):
        if not root:
            return 0
        left = self.getMax(root.left) + 1
        right = self.getMax(root.right) + 1
        
        self.max = max(self.max, left+right -2)
        return max(left, right)
        