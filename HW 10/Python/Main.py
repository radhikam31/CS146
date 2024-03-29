from Solution import Solution
from TreeNode import TreeNode

if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(4)
    root1.left = TreeNode(3)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(9)

    result1 = solution.levelOrder(root1)
    print("Test Case 1 Output:", result1) # Test Case 1 Output: [[4], [3, 8], [1, 5, 9]]

    root2 = None

    result2 = solution.levelOrder(root2)
    print("Test Case 2 Output:", result2) # Test Case 2 Output: []
