/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null)
            return false;
        if (root.left == null && root.right == null)
            return sum == root.val;
        if (root.left != null && hasPathSum(root.left, sum - root.val) || root.right != null && hasPathSum(root.right, sum - root.val))
            return true;
        return false;
    }
}