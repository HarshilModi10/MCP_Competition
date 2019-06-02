# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not q and not p:
            return True
        if not q or not p or q.val != p.val:
            return False
        right = self.isSameTree(p.left, q.left)
        left = self.isSameTree(p.right, q.right)
        
        return right and left
        

#Faster iterative solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack = [[p,q]]
        
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue                
            if not p or not q or p.val != q.val:
                return False
            stack.append([p.left, q.left])
            stack.append([p.right, q.right])
        
        return True
        
        