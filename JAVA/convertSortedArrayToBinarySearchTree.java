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
    public TreeNode sortedArrayToBST(int[] num) {
        return buildBST(0, num.length-1, num);
    }
    
    public TreeNode buildBST(int start, int end, int[] num){
        if (start > end)
            return null;
        int mid = (start + end) / 2;
        TreeNode root = new TreeNode(num[mid]);
        root.left = buildBST(start, mid - 1, num);
        root.right = buildBST(mid + 1, end, num);
        return root;
    }
}