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
    public int minDepth(TreeNode root) {
        if (root == null)
            return 0;
        int depth = 1;
        Set<TreeNode> currentLevel= new HashSet<TreeNode>();
        Set<TreeNode> nextLevel= new HashSet<TreeNode>(), temp;
        currentLevel.add(root);
        TreeNode cur;
        Iterator<TreeNode> iterator = currentLevel.iterator();
        while (iterator.hasNext()){
            cur = iterator.next();
            if (cur.left == null && cur.right == null)
                return depth;
            if (cur.left != null)
                nextLevel.add(cur.left);
            if (cur.right != null)
                nextLevel.add(cur.right);
            if (!iterator.hasNext()){
                depth++;
                temp = currentLevel;
                currentLevel = nextLevel;
                nextLevel = temp;
                iterator = currentLevel.iterator();
            }
        }
        return depth;
    }
}

/* TO DO: USE QUEUE INSTEAD */