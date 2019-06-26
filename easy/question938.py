# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        total = 0
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                total += node.val
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            elif L > node.val:
                if node.right:
                    stack.append(node.right)
            else:
                if node.left:
                    stack.append(node.left)
        return total
        