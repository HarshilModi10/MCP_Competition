# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return;
        self.inOrderTraversal(root)
        
        
        
        for i in range(1,len(self.res)):
            print(self.res[i].val)
            root.right = self.res[i]
            root.left = None
            root = root.right
    
    def inOrderTraversal(self, root):
        if not root:
            return 
        self.res.append(root)
        self.inOrderTraversal(root.left)
        self.inOrderTraversal(root.right)
        
    
        