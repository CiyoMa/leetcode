/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; left = null; right = null; }
 * }
 */
public class Solution {
    public List<TreeNode> generateTrees(int n) {
        return rangeHelper(1, n);
    }
    
    public List<TreeNode> rangeHelper(int start, int end){
        List<TreeNode> result = new ArrayList<TreeNode>(), left, right;
        if (start > end){
            result.add(null);
            return result;
        }
        if (start == end){
            result.add(new TreeNode(start));
            return result;
        }
        TreeNode root;
        for (int i = start; i <= end; i++){
            left = rangeHelper(start, i-1);
            right = rangeHelper(i+1, end);
            for (TreeNode l:left)
                for (TreeNode r:right){
                    root = new TreeNode(i);
                    root.left = l;
                    root.right = r;
                    result.add(root);
                }
        }
        return result;
    }
}