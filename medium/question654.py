# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.binary_tree(nums)
        
    def binary_tree(self, nums):
        
        if not nums:
            return None
        
        index = self.max_element(nums)
        
        
        node = TreeNode(nums[index])
        if index != 0:
            node.left = self.binary_tree(nums[:index])
        else:
            node.left = None
        if index != len(nums) - 1:   
            node.right = self.binary_tree(nums[index+1:])
        else:
            node.right = None
        
        return node
    
    def max_element(self, nums):
        index = 0
        
        for i, num in enumerate(nums):
            if nums[index] < num:
                index = i
                
        return index
            
    
        