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
    private int maxCrossNode;
    
    public int maxPathSum(TreeNode root) {
        if (root == null)
            return 0;
        maxCrossNode = root.val;        
        return Math.max(maxOneWayEndAtNode(root), maxCrossNode);
    }
    
    public int maxOneWayEndAtNode(TreeNode root){
        if (root == null)
            return 0;
        int left = maxOneWayEndAtNode(root.left);
        int right = maxOneWayEndAtNode(root.right);
        int tempCrossMax = root.val + left + right;
        int endMax =  root.val + Math.max(left, right);
        maxCrossNode = Math.max(tempCrossMax, Math.max(maxCrossNode, endMax));
        return Math.max(root.val, endMax);
    }
}