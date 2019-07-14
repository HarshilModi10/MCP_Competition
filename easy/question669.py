# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        if not root:
            return None        
        if root.val >R:
            return self.trimBST(root.left,L,R)
        if root.val < L:
            return self.trimBST(root.right, L, R)
        
        root.left = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right, L, R)
        return root

# Another solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root
        
        return self.helper(root, L, R)

    
    def helper(self, root, L, R):
        if not root:
            return None
        elif L <= root.val <= R:
            new_root = TreeNode(root.val)
            new_root.left = self.helper(root.left, L, R)
            new_root.right = self.helper(root.right, L, R)
            return new_root
        else:
            if root.val < L:
                return self.helper(root.right, L, R)
            else:
                return self.helper(root.left, L, R)
            
        
        