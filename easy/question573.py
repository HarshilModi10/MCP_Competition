# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.check = False
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not t:
            return False
        
        self.findNode(s,t)  
        
        
        return self.check
            
            
    
    def findNode(self,s,t):
        
        if not s or self.check:
            return None
        if s.val == t.val:
            self.check = self.checkSubTree(s,t)

        self.findNode(s.left,t)
        self.findNode(s.right,t)
        
    
    def checkSubTree(self, s, t):
        if not s and not t:
            return True
        if not s:
            return False
        if not t:
            return False
        
        if s.val == t.val:
            L = self.checkSubTree(s.left,t.left)
            R = self.checkSubTree(s.right, t.right)
            return (L and R)
        else:
            return False
        
        
        
        
        