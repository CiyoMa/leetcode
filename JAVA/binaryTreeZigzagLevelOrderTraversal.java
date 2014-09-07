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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        LinkedList<TreeNode> cur = new LinkedList<TreeNode>(), next;
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        if (root == null)
            return result;
        cur.add(root);
        boolean reverseFlag = true;
        while (!cur.isEmpty()){
            List<Integer> output = new ArrayList<Integer>();
            next = new LinkedList<TreeNode>();
            for (TreeNode n:cur){
                output.add(n.val);
                if (reverseFlag){
                    if (n.left != null)
                        next.addFirst(n.left);
                    if (n.right != null)
                        next.addFirst(n.right);
                }
                else{
                    if (n.right != null)
                        next.addFirst(n.right);
                    if (n.left != null)
                        next.addFirst(n.left);
                }
            }
            reverseFlag = !reverseFlag;
            cur = next;
            result.add(output);
        }
        return result;
    }
}