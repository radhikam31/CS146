public class Main {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        
        Solution solution = new Solution();
        TreeNode p = new TreeNode(3);
        TreeNode q = new TreeNode(1);
        TreeNode lca = solution.lowestCommonAncestor(root, p, q);
        System.out.println("Lowest common ancestor: " + lca.val);
    }
}
