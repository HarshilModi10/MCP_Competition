# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        inorder = sorted(preorder)
        
        return self.construct_binary_tree(preorder, inorder)
    
    def construct_binary_tree(self, preorder, inorder):
        
        if not inorder:
            return None
        node = TreeNode(preorder[0])
        val = preorder.pop(0)
        index = self.get_index(inorder, val)
        node.left = self.construct_binary_tree(preorder, inorder[:index])
        node.right = self.construct_binary_tree(preorder, inorder[index+1:])
        return node
        
        
        
    def get_index(self, inorder, val):
        
        for i, num in enumerate(inorder):
            if num == val:
                return i
        
        