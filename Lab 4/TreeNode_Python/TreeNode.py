class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root

def print_tree_inorder(root):
    if root is None:
        return
    print_tree_inorder(root.left)
    print(root.val, end=' ')
    print_tree_inorder(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    solution = Solution()
    inverted_root = solution.invertTree(root)
    
    print_tree_inorder(inverted_root) #Output: 3 1 5 2 4
