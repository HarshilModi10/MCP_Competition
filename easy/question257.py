# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans=[]
        self.dfs(root,'',ans)
        return ans
    
    def dfs(self,root,path,ans):
        if root:
            if not root.left and not root.right:
                ans.append(path+str(root.val))
            self.dfs(root.left,path+str(root.val)+'->',ans)
            self.dfs(root.right,path+str(root.val)+'->',ans)

        
        
        