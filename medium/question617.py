# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        
        stack = []
        stack.append((t1,t2))
        
        while stack:
            t = stack.pop()
            
            if (not t[0] or not t[1]):
                continue
            t[0].val += t[1].val
            
            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right,t[1].right))
        return t1
            
            