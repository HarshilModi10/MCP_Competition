# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        self.preorder = []
        
        self.preorder_traversal(root)
        return self.preorder
    
    def preorder_traversal(self, root):
        
        if not root:
            return None
        
        self.preorder.append(root.val)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
        
        
        