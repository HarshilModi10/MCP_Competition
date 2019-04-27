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

# faster solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # keep track of stack
        stack = []
        stack.append(root)
        while root:
            stack.append(root)
            root = root.left
        
        #Inorder traversal
        while stack:
            node = stack.pop()
            x = node.right
            while x:
                stack.append(x)
                x = x.left
            k -= 1
            
            if k == 0:
                return node.val
        
        return None

#reccursive solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        if not root:
            return None
        self.helper(root)
        return self.res
    
    def helper(self,node):
        
        if not node:
            return None
        
        self.helper(node.left)
        
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        
        self.helper(node.right)

            
        
            
            
        
        
            
        

        