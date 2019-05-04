# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        s1 = root.right
        s2 = root.left
        
        if s1 and s2:
            return self.is_symetric(s1,s2)
            
        if not s1 and not s2:
            return True
        return False
            
    # dfs to check for symmmetry
    def is_symetric(self,s1,s2):
        if s1.val != s2.val:
            return False
        elif s1.right and s1.left and s2.right and s2.left:
            result1 = self.is_symetric(s1.left,s2.right)
            result2 = self.is_symetric(s1.right, s2.left)
            return result1 and result2
        
        elif not s1.right and not s2.right and not s1.left and not s2.left:
            return True
        elif s1.right and s2.left and not s1.left and not s2.right:
            return self.is_symetric(s1.right, s2.left)
        elif s1.left and s2.right and not s1.right and not s2.left:
            return self.is_symetric(s1.left, s2.right)
        else:
            return False
            
        