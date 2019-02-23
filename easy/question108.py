# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        return self.sortBST(None, nums,0,len(nums)-1)
    
    def sortBST(self, root, nums, low, high):
        
        if low > high:
            return None
        
        mid = low + (high - low)/2
        
        root = TreeNode(nums[mid])
        root.left = self.sortBST(root, nums, low, mid-1)
        root.right = self.sortBST(root, nums, mid+1, high)
        
        return root
        