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
        
# faster solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        self.count = 0
        self.dic = {0:1}
        self.helperPathSum(root, sum, 0)
    
        return self.count 
    
    def helperPathSum(self, root, actual_sum, current_sum):
        if not root:
            return 
        
        current_sum += root.val
        target = current_sum - actual_sum
        #check if a path can be formed with previous elements
        if target in self.dic:
            self.count += self.dic[target]
        
        #add current sum to dictionary
        if current_sum in self.dic:
            self.dic[current_sum] += 1
        else:
            self.dic[current_sum] = 1
            
        self.helperPathSum(root.left, actual_sum, current_sum)
        self.helperPathSum(root.right, actual_sum, current_sum)
        
        #remove path after being done recursively
        self.dic[current_sum] -= 1
        
        
        
        
        