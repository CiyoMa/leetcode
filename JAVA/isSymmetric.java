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
    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;
        return areTwoNodeSymmetric(root.right, root.left);
    }
    public boolean areTwoNodeSymmetric(TreeNode left, TreeNode right){
        if (left == null && right == null)
            return true;
        if (left == null || right == null)
            return false;
        return left.val == right.val && areTwoNodeSymmetric(left.left, right.right) && areTwoNodeSymmetric(left.right, right.left);
    }
}