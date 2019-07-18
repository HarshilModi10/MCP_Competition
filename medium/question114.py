# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return;
        self.inOrderTraversal(root)
        
        
        
        for i in range(1,len(self.res)):
            print(self.res[i].val)
            root.right = self.res[i]
            root.left = None
            root = root.right
    
    def inOrderTraversal(self, root):
        if not root:
            return 
        self.res.append(root)
        self.inOrderTraversal(root.left)
        self.inOrderTraversal(root.right)
        
    #Faster solution 

    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = []
        stack.append(root)
        lastNode = TreeNode(-1)
        
        while stack:
            node = stack.pop()
            lastNode.right = node
            lastNode.left = None
            lastNode = lastNode.right
            
            if lastNode.right:
                stack.append(lastNode.right)
            if lastNode.left:
                stack.append(lastNode.left)
            
        
            
            
# another solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        order = []
        self.get_pre_order(root, order)
        
        dummyNode = current = TreeNode(0)
        for node in order:
            current.right = node
            current.left = None
            current = current.right
        
            
    
    
    def get_pre_order(self, root, order):
        if not root:
            return
        
        order.append(root)
        self.get_pre_order(root.left, order)
        self.get_pre_order(root.right, order)
    
        