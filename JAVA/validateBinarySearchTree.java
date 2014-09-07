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
    private TreeNode pre = null;
    
    public boolean isValidBST(TreeNode root) {
        return inorderCheck(root);
    }
    public boolean inorderCheck(TreeNode root){
        if (root == null)
            return true;
        if (!inorderCheck(root.left))
            return false;
        if (pre != null && pre.val >= root.val)
            return false;
        pre = root;
        return inorderCheck(root.right);
    }
}