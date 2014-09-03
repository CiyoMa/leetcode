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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> temp;
        List<List<Integer>> rest;
        
        if (root == null)
            return result;
        if (root.left == null && root.right == null && root.val == sum){
            temp = new ArrayList<Integer>();
            temp.add(root.val);
            result.add(temp);
        }
        if (root.left != null){
            rest = pathSum(root.left, sum - root.val);
            for (List<Integer> lst: rest)
                lst.add(0, root.val);
            result.addAll(rest);
        }
        if (root.right != null){
            rest = pathSum(root.right, sum - root.val);
            for (List<Integer> lst: rest)
                lst.add(0, root.val);
            result.addAll(rest);
        }
        return result;
    }
}