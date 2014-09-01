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
    public int sumNumbers(TreeNode root) {
        if (root == null)
            return 0;
        return dfs(root, 0);
    }
    public int dfs(TreeNode node, int cur){
        int result = 0;
        cur = cur*10 + node.val;
        if (node.left == null && node.right == null)
            return cur;
        if (node.left != null)
            result += dfs(node.left, cur);
        if (node.right != null)
            result += dfs(node.right, cur);
        return result;
    }
}