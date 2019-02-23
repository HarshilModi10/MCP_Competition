# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return self.total 
        
        self.getSum(root, sum)
        
        return self.total
        
        
    def getSum(self,root, sum):
        if not root:
            return 
        
        self.getTotal(root, sum)
        self.getSum(root.left,sum)
        self.getSum(root.right, sum)
        
        
    def getTotal(self,root, sum):
        
        if not root:
            return
        
        if root.val == sum:
            self.total += 1
        
        self.getTotal (root.left, sum - root.val)
        self.getTotal(root.right, sum - root.val)
        