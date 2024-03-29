import java.util.List;

public class Main {
    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        TreeNode root1 = new TreeNode(4);
        root1.left = new TreeNode(3);
        root1.right = new TreeNode(8);
        root1.left.left = new TreeNode(1);
        root1.left.right = new TreeNode(5);
        root1.right.right = new TreeNode(9);

        List<List<Integer>> result1 = solution.levelOrder(root1);
        System.out.println("Test Case 1 Output: " + result1);

        TreeNode root2 = null;

        List<List<Integer>> result2 = solution.levelOrder(root2);
        System.out.println("Test Case 2 Output: " + result2);
    }
}
