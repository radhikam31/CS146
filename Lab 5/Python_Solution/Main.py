from Solution import Solution
from TreeNode import TreeNode

# Main for testing
if __name__ == "__main__":
    # Example usage
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    solution = Solution()
    print("Is valid BST?", solution.isValidBST(root)) #Output is True
