# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.k = 0
        self.val = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k - 1
        self.small(root)
        return self.val
    
    def small(self,root):
        if not root:
            return 
        self.small(root.left)
        if self.k == 0:
            self.val = root.val
        self.k -= 1
        self.small(root.right)
        