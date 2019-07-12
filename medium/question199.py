# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = list()
        queue = [root]
        
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.pop(0)                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
        