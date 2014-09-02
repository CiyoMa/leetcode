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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<List<Integer>> reverse = new ArrayList<List<Integer>>();
        if (root == null)
            return result;
        ArrayList<TreeNode> cur = new ArrayList<TreeNode>();
        ArrayList<TreeNode> next = new ArrayList<TreeNode>();
        ArrayList<Integer> curLevel = new ArrayList<Integer>();
        cur.add(root);
        while (cur.size()>0){
            
            for (TreeNode n: cur){
                curLevel.add(n.val);
                if (n.left != null)
                    next.add(n.left);
                if (n.right!= null)
                    next.add(n.right);
            }
            cur = next;
            next = new ArrayList<TreeNode>();
            result.add(curLevel);
            curLevel = new ArrayList<Integer>();
        }
        for (int i = result.size()-1; i>=0; i--)
            reverse.add(result.get(i));
        return reverse;
    }
}