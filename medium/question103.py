# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None 
        
        queue = [root]
        zigzag_level = []
        reverse = False
        
        while queue:
            if reverse:
                reverse_queue = queue[::-1]
                zigzag_level.append([node.val for node in reverse_queue])
            else:
                zigzag_level.append([node.val for node in queue])
            
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            reverse = reverse == False
        return zigzag_level
                