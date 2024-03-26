class Solution:
    def isValidBST(self, root):
        return self._isValidBST(root, float('-inf'), float('inf'))
    
    def _isValidBST(self, node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (self._isValidBST(node.left, min_val, node.val) and
                self._isValidBST(node.right, node.val, max_val))
