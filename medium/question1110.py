class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        results = []
        
        if not to_delete:
            return [root]        
        else:
            self.helper(root, set(to_delete), results, None)
        return results
    
    def helper(self, root, to_delete, results, prev):
        if not root:
            return 
        
        if  root.val in to_delete:
            if prev and prev.left == root:
                prev.left = None
            elif prev and prev.right == root:
                prev.right = None
                
            self.helper(root.left, to_delete, results, None)
            self.helper(root.right, to_delete, results, None)
        else:
            if not prev:
                results.append(root)
            self.helper(root.left, to_delete, results, root)
            self.helper(root.right, to_delete, results, root)