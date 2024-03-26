from Solution import Solution
from TreeNode import TreeNode

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    solution = Solution()
    p = TreeNode(3)
    q = TreeNode(1)
    lca = solution.lowestCommonAncestor(root, p, q)
    print("Lowest common ancestor:", lca.val)
