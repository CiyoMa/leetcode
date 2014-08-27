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
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stk = new Stack<TreeNode>();
        if (root == null) return result;
        stk.push(root);
        TreeNode temp;
        while (!stk.empty()){
            temp = stk.pop();
            result.add(temp.val);
            if (temp.right != null) stk.push(temp.right);
            if (temp.left != null) stk.push(temp.left);
        }
        return result;
    }
}