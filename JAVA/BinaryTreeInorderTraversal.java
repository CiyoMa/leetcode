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
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stk = new Stack<TreeNode>();
        
        if (root == null) return result;
        stk.push(root);
        TreeNode cur;
        while (!stk.empty()){
            cur = stk.pop();
            while (cur != null){
                if (cur.right != null) stk.push(cur.right);
                stk.push(cur);
                cur = cur.left;
            }
            cur = stk.pop();
            while (!stk.empty() && cur.right == null){
                result.add(cur.val);
                cur = stk.pop();
            }
            result.add(cur.val);
        }
        return result;
    }
}