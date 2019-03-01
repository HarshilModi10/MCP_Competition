# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        
        queue = []
        final = []
        queue.append(root)        
        
        while queue:
            res = []
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            final.append(res)
        
        return final
                
                
       