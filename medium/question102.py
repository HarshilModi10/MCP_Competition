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
                
# another solution

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
        res = []
        level_val = []
        level = 0
        queue = []
        queue.append([root,0])
        
        while queue:
            node,local_level = queue.pop(0)
            if local_level > level:
                res.append(level_val)
                level_val = []
                level = local_level
                
            if node:
                level_val.append(node.val)
                queue.append([node.left,level+1])
                queue.append([node.right,level+1])
                
        return (res)
       
    #faster solution 

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
        levels = []
        queue = []
        queue.append(root)
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        
        return levels
        